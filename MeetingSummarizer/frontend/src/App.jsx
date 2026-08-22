import { Navigate, Route, Routes } from 'react-router-dom'
import AppShell from './components/AppShell.jsx'
import Dashboard from './pages/Dashboard.jsx'
import MeetingDetails from './pages/MeetingDetails.jsx'
import Upload from './pages/Upload.jsx'

export default function App() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route index element={<Dashboard />} />
        <Route path="upload" element={<Upload />} />
        <Route path="meetings/:meetingId" element={<MeetingDetails />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  )
}
