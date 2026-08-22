export default function StatCard({ icon: Icon, label, value, trend, accent }) {
  return (
    <article className="stat-card">
      <div className={`stat-icon ${accent}`}><Icon size={20} /></div>
      <div>
        <span className="eyebrow">{label}</span>
        <div className="stat-value-row"><strong>{value}</strong>{trend && <span>{trend}</span>}</div>
      </div>
    </article>
  )
}
