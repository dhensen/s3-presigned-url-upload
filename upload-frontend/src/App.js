import logo from "./AWS-S3-01.svg";
import "./App.css";
import ReactS3Uploader from "react-s3-uploader";
import React, { useState } from "react";

function App() {
  const [progress, setProgress] = useState(0);
  console.log(progress);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Kies een bestand om te uploaden:</p>
        <ReactS3Uploader
          signingUrl="http://localhost:8000/s3/sign"
          onProgress={(progressPercentage) => {
            console.log(progressPercentage);
            setProgress(progressPercentage);
          }}
        ></ReactS3Uploader>
        <ProgressBar progress={progress}></ProgressBar>
      </header>
    </div>
  );
}

function ProgressBar({ progress }) {
  let img = "";
  if (0 < progress && progress < 100) {
    img = (
      <img src="https://media.giphy.com/media/kH78ASiw737uGac1JX/giphy.gif"></img>
    );
  }
  return (
    <div>
      {img}Upload progress: {progress} %
    </div>
  );
}

export default App;
