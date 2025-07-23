import React from 'react';

function JobCard({ job, onDelete }) {
  return (
      <div className="card mb-3 shadow-sm">
          <div className="card-body">
              <h5 className="card-title">{job.title}</h5>
              <h6 className="card-subtitle mb-2 text-muted">{job.company} — {job.location}</h6>
              <p className="card-text">
                  <strong>Type:</strong> {job.job_type}<br/>
                  <strong>Posted:</strong> {job.posting_date}<br/>
                  <strong>Tags:</strong> {job.tags.join(', ')}
              </p>
              <button onClick={() => onDelete(job.id)} className="btn btn-danger">Delete</button>
          </div>
      </div>
  );
}

export default JobCard;
