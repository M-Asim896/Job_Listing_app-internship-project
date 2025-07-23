from flask import Blueprint, request, jsonify
from models import Job, db

routes = Blueprint('routes', __name__)

# ✅ Get all jobs (with optional filters and sorting)
@routes.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        query = Job.query

        job_type = request.args.get('job_type')
        location = request.args.get('location')
        tag = request.args.get('tag')
        sort = request.args.get('sort', 'posting_date_desc')

        if job_type:
            query = query.filter_by(job_type=job_type)
        if location:
            query = query.filter_by(location=location)
        if tag:
            query = query.filter(Job.tags.like(f'%{tag}%'))

        if sort == 'posting_date_asc':
            query = query.order_by(Job.posting_date.asc())
        else:
            query = query.order_by(Job.posting_date.desc())

        jobs = query.all()
        return jsonify([job.to_dict() for job in jobs]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Get a single job by ID
@routes.route('/jobs/<int:id>', methods=['GET'])
def get_job(id):
    job = Job.query.get(id)
    if job:
        return jsonify(job.to_dict()), 200
    else:
        return jsonify({"error": "Job not found"}), 404

# ✅ Create a new job
@routes.route('/jobs', methods=['POST'])
def create_job():
    data = request.json

    # Required fields check
    if not data.get("title") or not data.get("company") or not data.get("location"):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        job = Job(**data)
        db.session.add(job)
        db.session.commit()
        return jsonify(job.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Update existing job
@routes.route('/jobs/<int:id>', methods=['PUT'])
def update_job(id):
    job = Job.query.get(id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    try:
        for field in ['title', 'company', 'location', 'posting_date', 'job_type', 'tags']:
            if field in request.json:
                setattr(job, field, request.json[field])

        db.session.commit()
        return jsonify(job.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Delete a job
@routes.route('/jobs/<int:id>', methods=['DELETE'])
def delete_job(id):
    job = Job.query.get(id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    try:
        db.session.delete(job)
        db.session.commit()
        return jsonify({"message": "Job deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
