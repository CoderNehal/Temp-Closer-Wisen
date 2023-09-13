import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';

function CSVUploader() {
  const [csvData, setCSVData] = useState([]);

  const onDrop = (acceptedFiles) => {
    const file = acceptedFiles[0];
    const reader = new FileReader();

    reader.onload = (e) => {
      const text = e.target.result;
      // Parse the CSV data (you may want to use a CSV parsing library)
      const parsedData = text.split('\n').map((line) => line.split(','));

      setCSVData(parsedData);
    };

    reader.readAsText(file);
  };

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div>
      <div {...getRootProps()} className="dropzone">
        <input {...getInputProps()} />
        <p>Drag & drop a CSV file here, or click to select one</p>
      </div>
      {csvData.length > 0 && (
        <div>
          <h2>CSV Data</h2>
          <table>
            <thead>
              <tr>
                {csvData[0].map((cell, index) => (
                  <th key={index}>{cell}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {csvData.slice(1).map((row, rowIndex) => (
                <tr key={rowIndex}>
                  {row.map((cell, cellIndex) => (
                    <td key={cellIndex}>{cell}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default CSVUploader;
