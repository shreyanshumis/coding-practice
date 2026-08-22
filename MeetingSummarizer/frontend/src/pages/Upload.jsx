import { AlertCircle, ArrowLeft, Check, FileAudio, LoaderCircle, Sparkles, UploadCloud, X } from 'lucide-react'
import { useRef, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { meetingsApi } from '../services/api.js'

const acceptedExtensions = ['aac', 'mp3', 'wav', 'm4a', 'mp4', 'mpeg', 'mpga', 'ogg', 'flac', 'webm']

export default function Upload() {
  const inputRef = useRef(null)
  const navigate = useNavigate()
  const [file, setFile] = useState(null)
  const [title, setTitle] = useState('')
  const [dragging, setDragging] = useState(false)
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState('')

  const acceptFile = (nextFile) => {
    if (!nextFile) return
    const extension = nextFile.name.split('.').pop()?.toLowerCase()
    if (!acceptedExtensions.includes(extension)) {
      setError('Choose a supported audio or video file.')
      return
    }
    if (nextFile.size > 500 * 1024 * 1024) {
      setError('The recording must be smaller than 500 MB.')
      return
    }
    setFile(nextFile)
    setError('')
  }

  const upload = async () => {
    if (!file || submitting) return
    setSubmitting(true)
    setError('')
    const formData = new FormData()
    formData.append('audio', file)
    if (title.trim()) formData.append('title', title.trim())
    try {
      const result = await meetingsApi.upload(formData)
      navigate(`/meetings/${result.meeting_id}`)
    } catch (requestError) {
      setError(requestError.message)
      setSubmitting(false)
    }
  }

  return (
    <div className="page upload-page">
      <Link className="back-link" to="/"><ArrowLeft size={17} /> Back to meetings</Link>
      <section className="upload-layout">
        <div className="upload-copy">
          <span className="kicker"><Sparkles size={14} /> New analysis</span>
          <h1>Your meeting,<br /><em>distilled.</em></h1>
          <p>Upload your recording and SummaMeet will extract the moments that matter.</p>
          <div className="feature-list">
            {['Timestamped text transcript', 'Concise summary and key decisions', 'Action items with owners and deadlines'].map((item) => <div key={item}><span><Check size={15} /></span>{item}</div>)}
          </div>
        </div>
        <div className="upload-panel">
          <div className="panel-heading"><div><span className="eyebrow">Audio input</span><h2>Upload recording</h2></div><FileAudio size={24} /></div>
          <div
            className={dragging ? 'dropzone dragging' : file ? 'dropzone has-file' : 'dropzone'}
            onDragOver={(event) => { event.preventDefault(); setDragging(true) }}
            onDragLeave={() => setDragging(false)}
            onDrop={(event) => { event.preventDefault(); setDragging(false); acceptFile(event.dataTransfer.files[0]) }}
            onClick={() => !file && inputRef.current?.click()}
          >
            <input ref={inputRef} type="file" accept="audio/*,video/mp4,video/webm" hidden onChange={(event) => acceptFile(event.target.files[0])} />
            {file ? (
              <div className="selected-file">
                <span className="file-icon"><FileAudio size={26} /></span>
                <div><strong>{file.name}</strong><span>{(file.size / 1024 / 1024).toFixed(1)} MB · Ready to upload</span></div>
                <button className="icon-button" aria-label="Remove file" onClick={(event) => { event.stopPropagation(); setFile(null) }}><X size={18} /></button>
              </div>
            ) : (
              <><span className="upload-icon"><UploadCloud size={30} /></span><h3>Drop your recording here</h3><p>or <button type="button">browse your files</button></p><small>AAC, MP3, WAV, M4A, MP4, OGG, FLAC or WEBM · Up to 500 MB</small></>
            )}
          </div>
          <label className="field-label" htmlFor="meeting-title">Meeting title <span>Optional</span></label>
          <input className="text-input" id="meeting-title" value={title} onChange={(event) => setTitle(event.target.value)} placeholder="e.g. Weekly product sync" maxLength={180} />
          {error && <div className="form-error"><AlertCircle size={16} /> {error}</div>}
          <button className="button button-primary full-button" disabled={!file || submitting} onClick={upload}>{submitting ? <LoaderCircle className="spin" size={17} /> : <Sparkles size={17} />} {submitting ? 'Uploading…' : 'Analyze meeting'}</button>
          <p className="privacy-note">Your recording remains in this project’s local upload storage.</p>
        </div>
      </section>
    </div>
  )
}
