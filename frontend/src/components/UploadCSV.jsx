import { useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";

export default function UploadCsv() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState(false);

  async function handleGenerate(e) {
    e.preventDefault();
    setStatus("");
    setError(false);

    if (!file) {
      setStatus("Please select a topics.csv file.");
      setError(true);
      return;
    }

    setBusy(true);

    try {
      const formData = new FormData();
      formData.append("file", file);

      const res = await fetch(`${API_BASE}/generate`, {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        let msg = `Request failed (${res.status})`;
        try {
          const data = await res.json();
          if (data?.detail) msg = data.detail;
        } catch {}
        throw new Error(msg);
      }

      const blob = await res.blob();

      const cd = res.headers.get("content-disposition") || "";
      const match = cd.match(/filename="([^"]+)"/);
      const filename = match?.[1] || "lesson-notes.pdf";

      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);

      setStatus("PDF generated and downloaded!");
    } catch (err) {
      setStatus(err.message || "Something went wrong.");
      setError(true);
    } finally {
      setBusy(false);
    }
  }

  return (
    <div
      style={{
        background: "var(--card)",
        padding: 24,
        borderRadius: 14,
        boxShadow: "0 20px 40px rgba(0,0,0,0.45)",
      }}
    >
      <form onSubmit={handleGenerate} style={{ display: "grid", gap: 16 }}>
        <label
          style={{
            border: "2px dashed #1e293b",
            padding: 20,
            borderRadius: 12,
            cursor: "pointer",
            textAlign: "center",
            color: "var(--muted)",
          }}
        >
          {file ? (
            <span style={{ color: "var(--text)" }}>{file.name}</span>
          ) : (
            "Click to upload a .csv file with those headers"
          )}
          <input
            type="file"
            accept=".csv,text/csv"
            hidden
            onChange={(e) => setFile(e.target.files?.[0] ?? null)}
          />
        </label>

        <button
          type="submit"
          disabled={busy}
          style={{
            background: busy ? "#1e293b" : "var(--accent)",
            color: "#020617",
            fontWeight: 600,
            padding: "12px 16px",
            borderRadius: 10,
            border: "none",
            cursor: busy ? "not-allowed" : "pointer",
            transition: "all 0.2s ease",
          }}
        >
          {busy ? "Generating PDF…" : "Generate PDF"}
        </button>

        {status && (
          <div
            style={{
              marginTop: 8,
              color: error ? "var(--error)" : "var(--accent)",
              fontWeight: 500,
            }}
          >
            {status}
          </div>
        )}
      </form>
    </div>
  );
}