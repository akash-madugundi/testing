import Excel from "../ExcelSheet/Excel";
// import { Spinner } from "react-bootstrap";
import React, { useState } from "react";
import Papa from "papaparse";
import axios from "axios";
import "./Mainpage.css";
import jsPDF from "jspdf";
import { Button } from "react-bootstrap";
import html2canvas from "html2canvas";
import Codebox from "../Codebox";
import Table from "./Table";
import { RegExForm } from "../RegularExpression/form";
import { Row,Col } from "react-bootstrap";

const language = "python";
export default function MainPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [jsonData, setJsonData] = useState(null);
  const [analysisData, setAnalysisData] = useState(null);
  const [heatmapData, setHeatmapData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [bargraph_sp_miss, setBargraph_sp_miss] = useState(null);
  const [bargraph_nan, setBargraph_nan] = useState(null);
  const [bargraph_binning_cat, setBargraph_binning_cat] = useState(null);
  const [bargraph_class_imbal, setBargraph_class_imbal] = useState(null);
  // const [bargraph_sp_char, setBargraph_sp_char] = useState(null);
  // const [bargraph_hum_friendly, setBargraph_hum_friendly] = useState(null);
  // const [bargraph_tr_spaces, setBargraph_tr_spaces] = useState(null);
  const bargraph_sp_char = null;
  const bargraph_hum_friendly = null;
  const bargraph_tr_spaces = null;
  const [boxplot, setBoxplot] = useState(null);
  const [click, setClick] = useState(false);
  const [fileChosen, setFileChosen] = useState(false);

  const handleFileUpload = (event) => {
    setFileChosen(true);
    setSelectedFile(event.target.files[0]);
    // Added for excel Purpose, which itself is Okay
    Papa.parse(event.target.files[0], {
      header: true,
      skipEmptyLines: true,
      dynamicTyping: true,
      complete: function (result) {
        setJsonData(result.data);
      },
    });
  };

  const handleUpload = () => {
    setClick(true);
    setIsLoading(true); // we will set this to false when the response is received
    const formData = new FormData();
    formData.append("file", selectedFile);

    axios
      .post("http://127.0.0.1:5000/upload", formData)
      .then((response) => {
        console.log(response.data);
        setAnalysisData(response.data);
        setHeatmapData(response.data.heatmap);
        setBargraph_sp_miss(response.data.bargraph_sp_miss);
        setBargraph_nan(response.data.bargraph_nan);
        setBoxplot(response.data.outliers.plot);
        setBargraph_binning_cat(response.data.binning_cat.plot);
        setBargraph_class_imbal(response.data.imbalance.plot);
        // setBargraph_sp_char(response.data.sp_char.plot);
        // setBargraph_hum_friendly(response.data.hum_friendly.plot);
        // setBargraph_tr_spaces(response.data.tr_spaces.plot);
        console.log(response.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.log(error);
        setIsLoading(false);
      });
  };
  const handleDownload = () => {
    html2canvas(document.body).then((canvas) => {
      const imgData = canvas.toDataURL("image/png");
      const pdf = new jsPDF();
      pdf.addImage(imgData, "PNG", 0, 0);
      pdf.save("page-content.pdf");
    });
  };

  const downloadDataset = () => {
    axios
      .get('http://127.0.0.1:5000/download-dataset')
      .then((response) => {
        // Create a Blob from the response
        const blob = new Blob([response.data], { type: 'text/csv' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'refactored_dataset.csv'; // Specify the file name
        link.click(); // Trigger the download
      })
      .catch((error) => {
        console.log(error);
      });
  };
  const handleRefactorAll = () => {
    axios.post("http://127.0.0.1:5000/refactor/all")
      .then(response => {
        console.log("Refactor all data smells", response.data);
        // Handle response data
      })
      .catch(error => {
        console.log(error);
      });
  };
  
  const handleRefactorSpecialMissingValues = () => {
    axios.post("http://127.0.0.1:5000/refactor/special-missing-values")
    .then(response => {
      console.log("Refactor special missing values", response.data);
      // Handle response data
    })
    .catch(error => {
      console.log(error);
    });
  };
  
  const handleRefactorMissingValues = () => {
    axios.post("http://127.0.0.1:5000/refactor/missing-values")
    .then(response => {
      console.log("Refactor missing values", response.data);
      // Handle response data
    })
    .catch(error => {
      console.log(error);
    });
  };

  const handleIntToStr = () => {
    axios.post("http://127.0.0.1:5000/refactor/int-to-str")
    .then(response => {
      console.log("Refactor int-to-str", response.data);
      // Handle response data
    })
    .catch(error => {
      console.log(error);
    });
  };

  const handleUniqueValues = () => {
    axios.post("http://127.0.0.1:5000/refactor/unique_values")
    .then(response => {
      console.log("Refactor unique-values", response.data);
      // Handle response data
    })
    .catch(error => {
      console.log(error);
    });
  };
  
  const handlebinaryMissingvalues = () => {
    axios.post("http://127.0.0.1:5000/refactor/binary-missing-values")
    .then(response => {
      console.log("Refactor binary-missing-values", response.data);
      // Handle response data
    })
    .catch(error => {
      console.log(error);
    });
  };
  const handleRefactorBinningCategorical = () => {
    axios.post("http://127.0.0.1:5000/refactor/binning-categorical")
    .then(response => {
      console.log("Refactor binning categorical", response.data);
      // Handle response data
    })
    .catch(error => {
      console.log(error);
    });
  };
  
  const handleRefactorClassImbalance = () => {
    axios.post("http://127.0.0.1:5000/refactor/class-imbalance")
    .then(response => {
      console.log("Refactor class imbalance", response.data);
      // Handle response data
    })
    .catch(error => {
      console.log(error);
    });
  };
  
  const handleRefactorSpecialCharacters = () => {
    axios.post("http://127.0.0.1:5000/refactor/special-characters")
    .then(response => {
      console.log("Refactor special characters", response.data);
      // Handle response data
    })
    .catch(error => {
      console.log(error);
    });
  };
  
  const handleRefactorHumanFriendly = () => {
    axios.post("http://127.0.0.1:5000/refactor/human-friendly")
      .then(response => {
        console.log("Refactor human friendly", response.data);
        // Handle response data
      })
      .catch(error => {
        console.log(error);
      });
  };
  
  const handleRefactorTrailingSpaces = () => {
    axios.post("http://127.0.0.1:5000/refactor/trailing-spaces")
    .then(response => {
      console.log("Refactor trailing spaces", response.data);
      // Handle response data
    })
    .catch(error => {
      console.log(error);
    });
  };
  const handleRefactorDuplicateValues = () => {
    axios.post("http://127.0.0.1:5000/refactor/duplicate-values")
      .then(response => {
        console.log("Refactor duplicate values", response.data);
        // Handle response data
      })
      .catch(error => {
        console.log(error);
      });
  };
  
  const handleRefactorOutliers = () => {
    axios.post("http://127.0.0.1:5000/refactor/outliers")
      .then(response => {
        console.log("Refactor outliers", response.data);
        // Handle response data
      })
      .catch(error => {
        console.log(error);
      });
  };
  
  // const handleDownload = () => {
  //   setIsLoading(true); // off it when the pdf is downloaded, i.e after the pdf is saved
  //   const pdf = new jsPDF();
  //   const resultsContainer = document.getElementById("results-container");
  //   pdf.fromHTML(resultsContainer, 15, 15);
  //   // pdf.save('results.pdf');
  //   // setIsLoading(false);
  //   // it should be asynchoronous
  //   pdf
  //     .save("results.pdf")
  //     .then(() => {
  //       setIsLoading(false);
  //     })
  //     .catch((error) => {
  //       console.log(error);
  //       setIsLoading(false);
  //     });
  // };

  return (
    <div className="App">
      {isLoading && (
        <div className="loading-overlay">
          <div className="spinner"></div>
        </div>
      )}

      <div className="heading-text">
        <h1>SniffCSV DataSmell Detector</h1>
      </div>
      <div className="Intput-and-Btn">
        <br />
        <input
          type="file"
          name="file"
          accept=".csv"
          // Removed the onChange event handler of csv file
          onChange={handleFileUpload}
          className="input-file"
        />
        <button
          onClick={handleUpload}
        >
          Analysis
        </button>
      </div>
      {
        analysisData && (
          <div className="analysis-container">
           <Excel myjson={jsonData} />
           <h2 className="smells">IDENTIFIED SMELLS</h2>
           <div className="results">
              <div className="result">
                <h2 className="result-title">SPECIAL MISSING VALUES</h2>
                <Table className="table"
                col1Arr={analysisData.sp_missing_values.splmissCols}
                col2Arr={analysisData.sp_missing_values.missingPer}
                col1={"Column Name"}
                col2={"Missing Percentage"}
                smellName={"Special Missing Values"}
                />
                {bargraph_sp_miss && (
                <div className="imageBox">
                  <img
                    src={`data:image/png;base64,${bargraph_sp_miss}`}
                    alt="special missing values"
                  />
                  <div className="fig-text"> Special Missing Values</div>
                </div>
              )}
              <div className="d-flex justify-content-center my-2">
                <button onClick={handleRefactorSpecialMissingValues}>
                  Refactor Special Missing Values
                </button>
              </div>
              </div>
              <div className="result">
                <h2 className="result-title">MISSING VALUES</h2>
                <Table className="table"
                col1Arr={analysisData.missing_values.missCols}
                col2Arr={analysisData.missing_values.missPer}
                col1={"Column Name"}
                col2={"Missing Percentage"}
                smellName={"Missing Values"}
              />
              {bargraph_nan && (
                <div className="imageBox">
                  <img
                    src={`data:image/png;base64,${bargraph_nan}`}
                    alt="missing values"
                  />
                  <div className="fig-text">Missing Values</div>
                </div>
              )}
                   <div className="d-flex justify-content-center my-2">
                <button onClick={handleRefactorMissingValues}>
                  Refactor Missing Values
                </button>
              </div>
              </div>
              <div className="result">
                <h2 className="result-title">BINNING CATEGORICAL</h2>
                <Table className="table"
                col1Arr={analysisData.binning_cat.binCols}
                col2Arr={analysisData.binning_cat.unqVals}
                col1={"Column Name"}
                col2={"Unique values"}
                smellName={"Binning Categorical Columns"}
              />
              {bargraph_binning_cat && (
                <div className="image-box">
                  <img
                    src={`data:image/png;base64,${bargraph_binning_cat}`}
                    alt="binning_categorical"
                  />
                  <div className="fig-text">Binning Categorical</div>
                </div>
              )}
               <div className="d-flex justify-content-center my-2">
                <button onClick={handleRefactorBinningCategorical}>
                Refactor Binning Categorical
                </button>
              </div>
              </div>
              <div className="result">
                <h2 className="result-title">CLASS IMBALANCE</h2>
                <Table className="table"
                col1Arr={analysisData.imbalance.imbCols}
                col2Arr={analysisData.imbalance.imbRatio}
                col1={"Column Name"}
                col2={"Imbalance ratio"}
                smellName={"Categorical Columns with Class Imbalance"}
              />
              {bargraph_class_imbal &&  (
                <div className="image-box">
                  <img
                    src={`data:image/png;base64,${bargraph_class_imbal}`}
                    alt="class_imbalance"
                  />
                  <div className="fig-text"> Class Imbalance</div>
                </div>
              )}
               <div className="d-flex justify-content-center my-2">
                <button onClick={handleRefactorClassImbalance}>
                  Refactor Class Imbalance
                </button>
              </div>
              
              </div>
              <div className="result">
                <h2 className="result-title">SPECIAL CHARACTERS</h2>
                <ul className="data-smells-list">
                {splitIntoSentences(analysisData.sp_char.Info).map(
                  (sentence, index) => (
                    <li key={index}>{sentence}</li>
                  )
                )}
              </ul>
              {bargraph_sp_char && (
                <div className="image-box">
                  <img
                    src={`data:image/png;base64,${bargraph_sp_char}`}
                    alt="special_characters"
                  />
                  <div className="fig-text">{"Special Characters"}</div>
                </div>
              )}
                      <div className="d-flex justify-content-center my-2">
                <button onClick={handleRefactorSpecialCharacters}>
                  Refactor Special Characters
                </button>
              </div>
              </div>
              <div className="result">
                <h2 className="result-title">HUMAN FRIENDLY</h2>
                <ul className="data-smells-list">
                {splitIntoSentences(analysisData.hum_friendly.Info).map(
                  (sentence, index) => (
                    <li key={index}>{sentence}</li>
                  )
                )}
              </ul>
              {bargraph_hum_friendly && (
                <div className="image-box">
                  <img
                    src={`data:image/png;base64,${bargraph_hum_friendly}`}
                    alt="hum_friendly"
                  />
                  <div className="fig-text"> Human Friendly</div>
                </div>
              )}
                 <div className="d-flex justify-content-center my-2">
                <button onClick={handleRefactorHumanFriendly}>
                  Refactor Human Friendly
                </button>
              </div>
              </div>
              <div className="result">
                <h2 className="result-title">TRAILING SPACES</h2>
                <ul className="data-smells-list">
                {splitIntoSentences(analysisData.tr_spaces.Info).map(
                  (sentence, index) => (
                    <li key={index}>{sentence}</li>
                  )
                )}
              </ul>
              {bargraph_tr_spaces && (
                <div className="image-box">
                  <img
                    src={`data:image/png;base64,${bargraph_tr_spaces}`}
                    alt="tr_spaces"
                  />
                  <div className="fig-text">{"8) Trailing Spaces"}</div>
                </div>
              )}
               <div className="d-flex justify-content-center my-2">
                <button onClick={handleRefactorTrailingSpaces}>
                  Refactor Trailing Spaces
                </button>
              </div>
              </div>
              <div className="result">
                <h2 className="result-title">CORRELATED VALUES</h2>
                <div className="heatmap-container">
                {heatmapData && (
                  <div className="image-box">
                    <img
                      src={`data:image/png;base64,${heatmapData}`}
                      alt="correlation heatmap"
                    />
                    <div className="fig-text">Correlation Heatmap</div>
                  </div>
                )}
                <ul className="data-smells-list">
                  {analysisData.correlated.map((sentence, index) => (
                    <li key={index}>{sentence}</li>
                  ))}
                </ul>
              </div>
              </div>
              <div className="result">
                <h2 className="result-title">Outliers</h2>
                <ul className="data-smells-list">
                {splitIntoSentences(analysisData.outliers.Info).map(
                  (sentence, index) => (
                    <li key={index}>{sentence}</li>
                  )
                )}
              </ul>
              {boxplot && (
                <div className="img-box">
                  <img src={`data:image/png;base64,${boxplot}`} alt="boxplot" />
                  <div className="fig-text">Fig. Boxplot</div>
                </div>
              )}
                 <div className="d-flex justify-content-center my-2">
                <button onClick={handleRefactorOutliers}>
                  Refactor Outliers
                </button>
              </div>
              </div>
           
              <div className="result">
                <h2 className="result-title">DUPLICATE VALUES</h2>
                <ul className="data-smells-list">
                {splitIntoSentences(analysisData.duplicates).map(
                  (sentence, index) => (
                    <li key={index}>{sentence}</li>
                  )
                )}
              </ul>
              <div className="d-flex justify-content-center my-2">
                <button onClick={handleRefactorDuplicateValues}>
                  Refactor Duplicate Values
                </button>
              </div>
              </div>
              
              <div className="result">
                <h2 className="result-title">INTEGER AS STRING</h2>
                <ul className="data-smells-list">
                {splitIntoSentences(analysisData.int_to_str.Info).map(
                  (sentence, index) => (
                    <li key={index}>{sentence}</li>
                  )
                )}
              </ul>
              <div className="d-flex justify-content-center my-2">
                <button onClick={handleIntToStr}>
                  Refactor Integers as String
                </button>
              </div>
              </div>
              <div className="result">
                <h2 className="result-title">UNIQUE VALUES</h2>
                <ul className="data-smells-list">
                {splitIntoSentences(analysisData.unique_values.Info).map(
                  (sentence, index) => (
                    <li key={index}>{sentence}</li>
                  )
                )}
              </ul>
              <div className="d-flex justify-content-center my-2">
                <button onClick={handleUniqueValues}>
                  Refactor unique values
                </button>
              </div>
              </div>
              <div className="result">
                <h2 className="result-title">BINARY MISSING VALUES</h2>
                <ul className="data-smells-list">
                {splitIntoSentences(analysisData.binary_missing_values.Info).map(
                  (sentence, index) => (
                    <li key={index}>{sentence}</li>
                  )
                )}
              </ul>
              <div className="d-flex justify-content-center my-2">
                <button onClick={handlebinaryMissingvalues}>
                  Refactor binary missing values
                </button>
              </div>
              </div>
           </div>
           <div className="d-flex justify-content-center my-2">
                <button className=" w-100" onClick={downloadDataset}>
                  Download Refactored Dataset
                </button>
              </div>
          </div>
          
        )
      }
      {click && fileChosen && <RegExForm />}
    </div>
  );
}

function splitIntoSentences(text) {
  const sentences = text.split("\n");
  return sentences.filter((sentence) => sentence.length > 0);
}
