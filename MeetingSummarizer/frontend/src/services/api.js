const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? '/api'

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, options)
  if (!response.ok) {
    const body = await response.json().catch(() => ({}))
    throw new Error(body.detail ?? `Request failed with status ${response.status}`)
  }
  if (response.status === 204) return null
  return response.json()
}

export const meetingsApi = {
  list: () => request('/meetings'),
  get: (id) => request(`/meetings/${id}`),
  upload: (formData) => request('/meetings', { method: 'POST', body: formData }),
  remove: (id) => request(`/meetings/${id}`, { method: 'DELETE' }),
  updateAction: (meetingId, actionId, completed) => request(`/meetings/${meetingId}/actions/${actionId}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ completed }),
  }),
}
