import { ArrowUpRight, Clock3, ListChecks } from 'lucide-react'
import { Link } from 'react-router-dom'

export default function MeetingCard({ meeting }) {
  const processing = ['uploaded', 'transcribing', 'summarizing'].includes(meeting.status)
  const failed = meeting.status === 'failed'
  const date = new Date(meeting.created_at)
  const duration = meeting.duration_seconds ? `${Math.max(1, Math.round(meeting.duration_seconds / 60))} min` : 'Pending'

  return (
    <Link className="meeting-card" to={`/meetings/${meeting.id}`}>
      <div className="meeting-card-top">
        <span className="date-chip">{date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' })}</span>
        <span className={`status-pill ${failed ? 'failed' : processing ? 'processing' : 'completed'}`}><i /> {failed ? 'Failed' : processing ? meeting.status : 'Completed'}</span>
      </div>
      <div className="meeting-card-body">
        <h3>{meeting.title}</h3>
        <p>{failed ? 'Analysis could not be completed. Open this meeting for details.' : processing ? 'Your meeting is being transcribed and analyzed.' : meeting.summary}</p>
      </div>
      <div className="meeting-card-footer">
        <div className="meta-row">
          <span><Clock3 size={15} /> {duration}</span>
          <span><ListChecks size={15} /> {meeting.action_item_count} actions</span>
        </div>
        <span className="open-link">Open <ArrowUpRight size={16} /></span>
      </div>
    </Link>
  )
}
