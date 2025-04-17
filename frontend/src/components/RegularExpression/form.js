import React, { useState } from "react";
import axios from "axios";
import { Button } from "react-bootstrap";
import "./form.css";

export const RegExForm = () => {
  const [regex, setRegex] = useState("");
  const [colNo, setColNo] = useState(0);
  const [result, setResult] = useState("");
  const [count, setCount] = useState(null);
  const [checked, setChecked] = useState(false);

  const handleCheckboxChange = (event) => {
    setChecked(event.target.checked);
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post("http://127.0.0.1:5000/regularExp", {
        regex: regex,
        colNo: colNo,
      })
      .then((res) => {
        //console.log(res);
        setCount(res.data.count);
        setResult(res.data.percent);
        console.log(res.data);
      });
  };
  const handleChangeRegex = (e) => {
    setRegex(e.target.value);
  };

  const handleChangeColNum = (e) => {
    setColNo(e.target.value);
  };
  return (
    <div className="regex-container">
      <h1>Regular Expression Form</h1>
      <div className="form-container">
        <form className="form-box" onClick={handleSubmit}>
          <div className="reg-exp">
            <label>Enter the RegEx for column: &nbsp; </label>
            <input
              type="text"
              name="regexrow"
              className="field"
              onChange={handleChangeRegex}
            />
          </div>
          <div className="reg-exp">
            <label>Enter the Column number: &nbsp; &nbsp;</label>
            <input
              type="text"
              name="regexrow"
              className="field"
              onChange={handleChangeColNum}
            />
          </div>
          <div className="d-flex justify-content-center my-2">
            <button
              type="submit"
              // className="regex-btn align-items-center"
              // variant="primary"
            >
              Submit
            </button>
          </div>
          {/* {result ? <div>{result}</div> : null} */}
          {result ? (
            <div className="regex-results">
              <p>
                {/* split result */}
                {splitIntoSentences(result).map((sentence) => (
                  <div>{sentence}</div>
                ))}
              </p>
              {count ? <p>Number Of Matches:{count}</p> : null}
            </div>
          ) : null}
        </form>
      </div>
    </div>
  );
};

function splitIntoSentences(text) {
  const sentences = text.split("\n");
  return sentences.filter((sentence) => sentence.length > 0);
}
