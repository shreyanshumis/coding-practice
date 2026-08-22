import { AlertCircle, ArrowRight, CheckCircle2, Clock3, FileAudio, LoaderCircle, Plus, Sparkles } from 'lucide-react'
import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import MeetingCard from '../components/MeetingCard.jsx'
import StatCard from '../components/StatCard.jsx'
import { meetingsApi } from '../services/api.js'

export default function Dashboard() {
  const [meetings, setMeetings] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    let active = true
    const load = async () => {
      try {
        const result = await meetingsApi.list()
        if (active) {
          setMeetings(result)
          setError('')
        }
      } catch (requestError) {
        if (active) setError(requestError.message)
      } finally {
        if (active) setLoading(false)
      }
    }
    load()
    const timer = setInterval(load, 5000)
    return () => {
      active = false
      clearInterval(timer)
    }
  }, [])

  const stats = useMemo(() => {
    const completed = meetings.filter((meeting) => meeting.status === 'completed')
    const totalMinutes = completed.reduce((sum, meeting) => sum + (meeting.duration_seconds ?? 0) / 60, 0)
    return {
      meetings: completed.length,
      hours: (totalMinutes / 60).toFixed(1),
      actions: meetings.reduce((sum, meeting) => sum + meeting.action_item_count, 0),
    }
  }, [meetings])

  return (
    <div className="page dashboard-page">
      <section className="hero-section">
        <div>
          <span className="kicker"><Sparkles size={14} /> AI meeting intelligence</span>
          <h1>Turn every conversation<br />into <em>clear action.</em></h1>
          <p>Upload a meeting and get the transcript, summary, decisions, and next steps without replaying the whole recording.</p>
          <Link className="button button-primary hero-button" to="/upload"><Plus size={18} /> Upload a meeting</Link>
        </div>
        <div className="hero-art" aria-hidden="true">
          <div className="orb orb-one" /><div className="orb orb-two" />
          <div className="wave-card">
            <div className="wave-card-head"><span className="live-dot" /> Audio intelligence <span>Ready</span></div>
            <div className="waveform">{[28,44,20,56,34,68,42,76,30,62,48,82,38,56,24,70,44,64,28,52,36,72,42,58,26,48,34,62].map((height, index) => <i key={index} style={{ height }} />)}</div>
            <div className="analysis-row"><span className="avatar-stack"><b>ASR</b><b>AI</b></span><span>Transcript to structured action</span><CheckCircle2 size={18} /></div>
          </div>
        </div>
      </section>

      <section className="stats-grid">
        <StatCard icon={FileAudio} label="Meetings analyzed" value={stats.meetings} accent="violet" />
        <StatCard icon={Clock3} label="Recorded hours" value={stats.hours} accent="peach" />
        <StatCard icon={CheckCircle2} label="Action items found" value={stats.actions} accent="mint" />
      </section>

      <section className="content-section">
        <div className="section-heading">
          <div><span className="eyebrow">Your workspace</span><h2>Recent meetings</h2></div>
          {meetings.length > 4 && <span className="meeting-count">{meetings.length} total <ArrowRight size={15} /></span>}
        </div>
        {loading && <div className="state-panel"><LoaderCircle className="spin" size={26} /><p>Loading meetings</p></div>}
        {!loading && error && <div className="state-panel error"><AlertCircle size={26} /><h3>Backend unavailable</h3><p>{error}</p><small>Start the project with npm run dev from the repository root.</small></div>}
        {!loading && !error && meetings.length === 0 && <div className="state-panel empty-dashboard"><FileAudio size={30} /><h3>No meetings yet</h3><p>Upload your first recording to generate a transcript and action-oriented summary.</p><Link className="button button-primary" to="/upload"><Plus size={17} /> Upload meeting</Link></div>}
        {!loading && !error && meetings.length > 0 && <div className="meeting-grid">{meetings.map((meeting) => <MeetingCard key={meeting.id} meeting={meeting} />)}</div>}
      </section>
    </div>
  )
}
