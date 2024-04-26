import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import QuizSubjectList from "./QuizSubjectList";
function Quiz() {
  const [subjects, setSubjects] = useState(sampleSubjects);

  return (
    <>
      {/* <h1>Quiz</h1> */}
      <div className="m-5">
        <QuizSubjectList subjects={subjects} />
      </div>
    </>
  );
}
const sampleSubjects = [
  {
    name: "english",
  },
  {
    name: "Maths",
  },
  {
    name: "CS",
  },
];

export default Quiz;
