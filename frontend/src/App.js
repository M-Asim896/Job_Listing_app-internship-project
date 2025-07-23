import React from 'react';
import JobList from './components/JobList';

function App() {
  return (
    <div className="container mt-4">
      <h1 className="text-center text-primary mb-4">Job Listing Board</h1>
      <JobList />
    </div>
  );
}

export default App;
