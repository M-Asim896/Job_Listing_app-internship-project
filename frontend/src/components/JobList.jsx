import React, { useEffect, useState } from 'react';
import { api } from '../api';
import JobCard from './JobCard';
import JobForm from './JobForm';
import FilterBar from './FilterBar';

function JobList() {
  const [jobs, setJobs] = useState([]);
  const [filters, setFilters] = useState({
    job_type: '',
    location: '',
    tag: '',
    sort: 'posting_date_desc'
  });

  const loadJobs = async () => {
    const query = new URLSearchParams(filters).toString();
    const res = await api.get(`/jobs?${query}`);
    setJobs(res.data);
  };

  useEffect(() => {
    loadJobs();
  }, []);

  const handleDelete = async (id) => {
    await api.delete(`/jobs/${id}`);
    loadJobs();
  };

  return (
    <>
      <h2>Add New Job</h2>
      <JobForm onSuccess={loadJobs} />
      <h2>Filter Jobs</h2>
      <FilterBar filters={filters} setFilters={setFilters} onFilter={loadJobs} />
      <h2>Job Listings</h2>
      {jobs.length === 0 ? (
        <p>No jobs found</p>
      ) : (
        jobs.map((job) => (
          <JobCard key={job.id} job={job} onDelete={handleDelete} />
        ))
      )}
    </>
  );
}

export default JobList;
