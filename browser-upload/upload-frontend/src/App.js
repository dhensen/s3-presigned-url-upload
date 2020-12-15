import logo from "./AWS-S3-01.svg";
import "./App.css";
import ReactS3Uploader from "react-s3-uploader";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Kies een bestand om te uploaden:</p>
        <ReactS3Uploader signingUrl="http://localhost:8000/s3/sign"></ReactS3Uploader>
      </header>
    </div>
  );
}

export default App;
