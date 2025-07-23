import React, { useState } from 'react';
import { api } from '../api';

function JobForm({ onSuccess }) {
  const [form, setForm] = useState({
    title: '',
    company: '',
    location: '',
    posting_date: '',
    job_type: '',
    tags: ''
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/jobs', form);
      setForm({ title: '', company: '', location: '', posting_date: '', job_type: '', tags: '' });
      onSuccess();
    } catch (err) {
      alert('Error adding job');
    }
  };

  return (
      <form onSubmit={handleSubmit} className="row g-3 mb-4">
        {Object.keys(form).map((field) => (
            <div key={field} className="col-md-4">
              <input
                  type="text"
                  name={field}
                  placeholder={field}
                  className="form-control"
                  value={form[field]}
                  onChange={handleChange}
                  required
              />
            </div>
        ))}
        <div className="col-12">
          <button type="submit" className="btn btn-success">Add Job</button>
        </div>
      </form>
  );
}

export default JobForm;
