import UploadCsv from "./components/UploadCsv";

export default function App() {
  return (
    <div
      style={{
        maxWidth: 760,
        margin: "60px auto",
        padding: "0 16px",
      }}
    >
      <h1 style={{ fontSize: 36, marginBottom: 8 }}>
        PDF Lesson Generator
      </h1>

      <p style={{ color: "var(--muted)", marginBottom: 32 }}>
        Upload a <code>topics.csv</code> file with columns{" "}
        <b>Order</b>, <b>Topic</b>, and <b>Pages</b>.
      </p>

      <UploadCsv />
    </div>
  );
}