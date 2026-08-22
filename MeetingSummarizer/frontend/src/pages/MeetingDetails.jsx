import { AlertCircle, ArrowLeft, CalendarDays, Check, CheckCircle2, Clock3, Download, FileText, ListChecks, LoaderCircle, Sparkles, Trash2 } from 'lucide-react'
import { useEffect, useState } from 'react'
import { Link, useNavigate, useParams } from 'react-router-dom'
import { meetingsApi } from '../services/api.js'

const tabs = [
  { id: 'summary', label: 'Summary', icon: Sparkles },
  { id: 'transcript', label: 'Transcript', icon: FileText },
  { id: 'decisions', label: 'Decisions', icon: CheckCircle2 },
  { id: 'actions', label: 'Actions', icon: ListChecks },
]

export default function MeetingDetails() {
  const { meetingId } = useParams()
  const navigate = useNavigate()
  const [meeting, setMeeting] = useState(null)
  const [activeTab, setActiveTab] = useState('summary')
  const [error, setError] = useState('')

  useEffect(() => {
    let active = true
    let timer
    const load = async () => {
      try {
        const result = await meetingsApi.get(meetingId)
        if (!active) return
        setMeeting(result)
        setError('')
        if (['uploaded', 'transcribing', 'summarizing'].includes(result.status)) timer = setTimeout(load, 2500)
      } catch (requestError) {
        if (active) setError(requestError.message)
      }
    }
    load()
    return () => {
      active = false
      clearTimeout(timer)
    }
  }, [meetingId])

  const toggleAction = async (action) => {
    const completed = !action.completed
    setMeeting((current) => ({ ...current, action_items: current.action_items.map((item) => item.id === action.id ? { ...item, completed } : item) }))
    try {
      await meetingsApi.updateAction(meeting.id, action.id, completed)
    } catch (requestError) {
      setError(requestError.message)
      setMeeting((current) => ({ ...current, action_items: current.action_items.map((item) => item.id === action.id ? action : item) }))
    }
  }

  const removeMeeting = async () => {
    if (!window.confirm('Delete this meeting and its uploaded recording?')) return
    await meetingsApi.remove(meeting.id)
    navigate('/')
  }

  if (error && !meeting) return <PageError message={error} />
  if (!meeting) return <div className="page loading-page"><LoaderCircle className="spin" size={30} /><p>Loading meeting</p></div>
  if (['uploaded', 'transcribing', 'summarizing'].includes(meeting.status)) return <ProcessingMeeting meeting={meeting} />
  if (meeting.status === 'failed') return <FailedMeeting meeting={meeting} removeMeeting={removeMeeting} />

  const exportMeeting = () => {
    const actions = meeting.action_items.map((item) => `- ${item.task} | Owner: ${item.assignee ?? 'Not specified'} | Due: ${item.deadline ?? 'Not specified'}`).join('\n')
    const content = `${meeting.title}\n\nSUMMARY\n${meeting.summary}\n\nKEY POINTS\n${meeting.key_points.map((item) => `- ${item}`).join('\n')}\n\nDECISIONS\n${meeting.decisions.map((item) => `- ${item}`).join('\n')}\n\nACTION ITEMS\n${actions}\n\nTRANSCRIPT\n${meeting.transcript}`
    const url = URL.createObjectURL(new Blob([content], { type: 'text/plain' }))
    const anchor = document.createElement('a')
    anchor.href = url
    anchor.download = `${meeting.title.replace(/[^a-z0-9]+/gi, '-').toLowerCase()}.txt`
    anchor.click()
    URL.revokeObjectURL(url)
  }

  return (
    <div className="page details-page">
      <Link className="back-link" to="/"><ArrowLeft size={17} /> Back to meetings</Link>
      <section className="meeting-header">
        <div>
          <div className="status-line"><span className="status-pill completed"><i /> Completed</span><span>{formatDate(meeting.created_at)}</span></div>
          <h1>{meeting.title}</h1>
          <div className="meeting-meta"><span><CalendarDays size={16} /> {formatDate(meeting.created_at, true)}</span><span><Clock3 size={16} /> {formatDuration(meeting.duration_seconds)}</span><span><FileText size={16} /> {meeting.language?.toUpperCase() ?? 'Auto-detected'}</span></div>
        </div>
        <div className="header-actions"><button className="button button-secondary" onClick={exportMeeting}><Download size={17} /> Export</button><button className="button button-danger" onClick={removeMeeting}><Trash2 size={17} /> Delete</button></div>
      </section>
      {error && <div className="inline-error"><AlertCircle size={16} /> {error}</div>}
      <div className="tab-bar">{tabs.map(({ id, label, icon: Icon }) => <button key={id} className={activeTab === id ? 'active' : ''} onClick={() => setActiveTab(id)}><Icon size={17} /> {label}{id === 'actions' && <span>{meeting.action_items.length}</span>}</button>)}</div>
      <section className="detail-content">
        {activeTab === 'summary' && <SummaryTab meeting={meeting} setActiveTab={setActiveTab} toggleAction={toggleAction} />}
        {activeTab === 'transcript' && <TranscriptTab meeting={meeting} />}
        {activeTab === 'decisions' && <DecisionsTab meeting={meeting} />}
        {activeTab === 'actions' && <ActionsTab actions={meeting.action_items} toggleAction={toggleAction} />}
      </section>
    </div>
  )
}

function SummaryTab({ meeting, setActiveTab, toggleAction }) {
  return (
    <div className="detail-grid">
      <div className="detail-main">
        <article className="summary-card accent-card"><span className="card-label"><Sparkles size={15} /> Executive summary</span><p>{meeting.summary}</p></article>
        <article className="summary-card"><span className="card-label">Key discussion points</span><ul className="key-point-list">{meeting.key_points.map((point, index) => <li key={point}><span>{String(index + 1).padStart(2, '0')}</span><p>{point}</p></li>)}</ul></article>
        <article className="summary-card"><div className="card-heading-row"><span className="card-label">Action items</span>{meeting.action_items.length > 2 && <button onClick={() => setActiveTab('actions')}>View all</button>}</div>{meeting.action_items.length ? <div className="action-list compact">{meeting.action_items.slice(0, 2).map((action) => <ActionRow key={action.id} action={action} toggleAction={toggleAction} />)}</div> : <EmptyCopy text="No action items were identified." />}</article>
      </div>
      <aside className="detail-aside">
        <article className="summary-card"><span className="card-label">Key decisions</span>{meeting.decisions.length ? <div className="decision-list">{meeting.decisions.map((decision) => <div key={decision}><span><Check size={14} /></span><p>{decision}</p></div>)}</div> : <EmptyCopy text="No explicit decisions were identified." />}</article>
        <article className="summary-card"><span className="card-label">Unresolved questions</span>{meeting.unresolved_questions.length ? <ul className="simple-list">{meeting.unresolved_questions.map((question) => <li key={question}>{question}</li>)}</ul> : <EmptyCopy text="No unresolved questions were identified." />}</article>
      </aside>
    </div>
  )
}

function TranscriptTab({ meeting }) {
  return <article className="summary-card transcript-card"><div className="card-heading-row"><div><span className="card-label">Full transcript</span><p className="muted-copy">Timestamped by speech segment</p></div></div><div className="transcript-list">{meeting.transcript_segments.length ? meeting.transcript_segments.map((line, index) => <div className="transcript-line api-transcript-line" key={`${line.start}-${index}`}><span className="timestamp">{toTimestamp(line.start)}</span><p>{line.text}</p></div>) : <div className="plain-transcript">{meeting.transcript}</div>}</div></article>
}

function DecisionsTab({ meeting }) {
  return <article className="summary-card"><span className="card-label">Decisions made</span>{meeting.decisions.length ? <div className="large-decision-list">{meeting.decisions.map((decision, index) => <div key={decision}><span><CheckCircle2 size={21} /></span><div><small>Decision {String(index + 1).padStart(2, '0')}</small><p>{decision}</p></div></div>)}</div> : <EmptyCopy text="No explicit decisions were identified in this meeting." />}</article>
}

function ActionsTab({ actions, toggleAction }) {
  return <article className="summary-card"><div className="card-heading-row"><div><span className="card-label">Action items</span><p className="muted-copy">{actions.filter((action) => !action.completed).length} remaining</p></div></div>{actions.length ? <div className="action-list">{actions.map((action) => <ActionRow key={action.id} action={action} toggleAction={toggleAction} />)}</div> : <EmptyCopy text="No action items were identified in this meeting." />}</article>
}

function ActionRow({ action, toggleAction }) {
  return <div className={action.completed ? 'action-row done' : 'action-row'}><button className="check-button" aria-label={action.completed ? 'Mark incomplete' : 'Mark complete'} onClick={() => toggleAction(action)}>{action.completed && <Check size={14} />}</button><div className="action-copy"><strong>{action.task}</strong><span>{action.assignee ?? 'No owner specified'}</span></div><div className="action-due"><small>Due {action.deadline ?? 'not specified'}</small>{action.source_timestamp && <span>{action.source_timestamp}</span>}</div></div>
}

function ProcessingMeeting({ meeting }) {
  const labels = { uploaded: 'Preparing upload', transcribing: 'Transcribing audio', summarizing: 'Generating summary' }
  const progress = { uploaded: 18, transcribing: 52, summarizing: 82 }
  return <div className="processing-page"><Link className="back-link" to="/"><ArrowLeft size={17} /> Back to meetings</Link><div className="processing-card"><div className="processing-visual"><FileText size={32} /><span /></div><span className="kicker"><Sparkles size={14} /> Analysis in progress</span><h1>{meeting.title}</h1><p>{labels[meeting.status]}. You can leave this page and return while processing continues.</p><div className="progress-track"><span style={{ width: `${progress[meeting.status]}%` }} /></div><div className="processing-steps"><span className="complete"><Check size={14} /> Uploaded</span><span className={meeting.status === 'transcribing' ? 'active' : meeting.status === 'summarizing' ? 'complete' : ''}>Transcribing</span><span className={meeting.status === 'summarizing' ? 'active' : ''}>Summarizing</span></div></div></div>
}

function FailedMeeting({ meeting, removeMeeting }) {
  return <div className="processing-page"><Link className="back-link" to="/"><ArrowLeft size={17} /> Back to meetings</Link><div className="processing-card failed-card"><div className="processing-visual failed"><AlertCircle size={32} /></div><span className="kicker">Analysis failed</span><h1>{meeting.title}</h1><p>{meeting.error_message || 'The recording could not be processed.'}</p><div className="failure-actions"><Link className="button button-primary" to="/upload">Try another recording</Link><button className="button button-danger" onClick={removeMeeting}><Trash2 size={17} /> Delete</button></div></div></div>
}

function PageError({ message }) {
  return <div className="page loading-page"><AlertCircle size={30} /><h2>Meeting unavailable</h2><p>{message}</p><Link className="button button-primary" to="/">Back to meetings</Link></div>
}

function EmptyCopy({ text }) {
  return <p className="empty-copy">{text}</p>
}

function formatDate(value, includeTime = false) {
  return new Date(value).toLocaleString(undefined, includeTime ? { dateStyle: 'medium', timeStyle: 'short' } : { dateStyle: 'medium' })
}

function formatDuration(seconds) {
  if (!seconds) return 'Duration unavailable'
  const minutes = Math.floor(seconds / 60)
  const remaining = Math.round(seconds % 60)
  return `${minutes}:${String(remaining).padStart(2, '0')}`
}

function toTimestamp(seconds) {
  const minutes = Math.floor(seconds / 60)
  const remaining = Math.floor(seconds % 60)
  return `${String(minutes).padStart(2, '0')}:${String(remaining).padStart(2, '0')}`
}
