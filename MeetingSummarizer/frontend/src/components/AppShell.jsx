import { Plus } from 'lucide-react'
import { Link, Outlet } from 'react-router-dom'

export default function AppShell() {
  return (
    <div className="app-shell">
      <div className="ambient ambient-one" />
      <div className="ambient ambient-two" />
      <header className="topbar">
        <Link className="brand" to="/" aria-label="SummaMeet home">
          <span className="brand-wordmark">summameet</span>
        </Link>
        <Link className="button button-primary compact-upload" to="/upload"><Plus size={17} /> New meeting</Link>
      </header>
      <main><Outlet /></main>
    </div>
  )
}
