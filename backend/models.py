from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    company = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    posting_date = db.Column(db.String(50), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    tags = db.Column(db.String(250))  # Comma-separated string

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'posting_date': self.posting_date,
            'job_type': self.job_type,
            'tags': self.tags.split(",") if self.tags else []
        }
