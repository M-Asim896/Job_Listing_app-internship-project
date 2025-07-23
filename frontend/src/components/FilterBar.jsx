import React from 'react';

function FilterBar({ filters, setFilters, onFilter }) {
  const handleChange = (e) => {
    setFilters({ ...filters, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onFilter(); // triggers job reload with filters
  };

  return (
    <form onSubmit={handleSubmit} className="row g-2 mb-4">
      <div className="col-md-3">
        <select className="form-select" name="job_type" value={filters.job_type} onChange={handleChange}>
          <option value="">All Job Types</option>
          <option value="Full-time">Full-time</option>
          <option value="Part-time">Part-time</option>
          <option value="Internship">Internship</option>
        </select>
      </div>
      <div className="col-md-3">
        <input
          type="text"
          className="form-control"
          name="location"
          placeholder="Location"
          value={filters.location}
          onChange={handleChange}
        />
      </div>
      <div className="col-md-3">
        <input
          type="text"
          className="form-control"
          name="tag"
          placeholder="Tag (e.g. Python)"
          value={filters.tag}
          onChange={handleChange}
        />
      </div>
      <div className="col-md-2">
        <select className="form-select" name="sort" value={filters.sort} onChange={handleChange}>
          <option value="posting_date_desc">Newest First</option>
          <option value="posting_date_asc">Oldest First</option>
        </select>
      </div>
      <div className="col-md-1">
        <button type="submit" className="btn btn-primary w-100">Filter</button>
      </div>
    </form>
  );
}

export default FilterBar;
