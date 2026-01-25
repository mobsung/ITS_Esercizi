from flask import Flask, jsonify, request, url_for

from Classi.medicalVisit import MedicalVisit
from Classi.diagnosticExam import DiagnosticExam
from Classi.clinicHub import ClinicHub

app = Flask(__name__)

clinic: ClinicHub = ClinicHub()

@app.route('/')
def home():
    home_out = {
        'message': "Clinic Booking Hub API",
        'links': {
            'get_all_bookings': url_for("get_all_bookings"),
            'get_booking': url_for("get_booking", booking_id="V123"),
            'get_estimated_wait': url_for('get_estimated_wait', booking_id="V123", factor=1.5),
        }
    }

    return jsonify(home_out)


@app.get('/bookings')
def get_all_bookings():
    return jsonify(clinic.list_all())

@app.get('/bookings/<string:booking_id>')
def get_booking(booking_id: str):
    if clinic.get(booking_id):
        return jsonify(clinic.get(booking_id).info())
    return jsonify({"error": "booking not found"}), 404

@app.get('/bookings/<string:booking_id>/wait/<float:factor>')
def get_estimated_wait(booking_id: str, factor:float):
    if clinic.get(booking_id):
        booking = clinic.get(booking_id)
        return jsonify({
            "booking_id": booking_id,
            "booking_type": booking.booking_type(),
            "factor": factor,
            "estimated_wait_minutes": booking.estimated_wait()
        })
    return jsonify({"error": "booking not found"}), 404

def create_booking(new_booking) -> MedicalVisit | DiagnosticExam:
    if new_booking["type"] == "visit":
        booking: MedicalVisit = MedicalVisit(
            booking_id=new_booking["booking_id"],
            patient_name=new_booking["patient_name"],
            doctor=new_booking["doctor"],
            department=new_booking["department"],
            date=new_booking["date"],
            time=new_booking["time"],
            status=new_booking["status"],
            visit_reason=new_booking["visit_reason"],
            first_time=new_booking["first_time"]
        )
    elif new_booking["type"] == "exam":
        booking: DiagnosticExam = DiagnosticExam(
            booking_id=new_booking["booking_id"],
            patient_name=new_booking["patient_name"],
            doctor=new_booking["doctor"],
            department=new_booking["department"],
            date=new_booking["date"],
            time=new_booking["time"],
            status=new_booking["status"],
            exam_type=new_booking["exam_type"],
            requires_fasting=new_booking["requires_fasting"]
        )
    
    return booking

def validate_json(new_booking) -> bool:
    checks: list[str] = ["booking_id", "patient_name", "doctor", "department", "date", "time", "status"]

    for check in checks:
        if check not in new_booking:
            return jsonify({"errore: campi mancanti"}), 400
        
    if new_booking["type"] != "visit" and new_booking["type"] != "exam":
        return jsonify({"errore: tipo non riconosciuto"}), 400
    
    if new_booking["type"] == "visit" and "visit_reason" not in new_booking and "first_time" not in new_booking:
        return jsonify({"errore: campi mancanti"}), 400
    
    if new_booking["type"] == "exam" and "exam_type" not in new_booking and "requires_fasting" not in new_booking:
        return jsonify({"errore: campi mancanti"}), 400
    
    return True

@app.post('/bookings')
def post_booking():
    new_booking = request.get_json()

    if validate_json(new_booking):
        booking = create_booking(new_booking)
        clinic.add(booking)
        return jsonify(booking.info())

@app.put('/bookings/<string:booking_id>')
def put_booking(booking_id: str):
    new_booking = request.get_json()
    if clinic.get(booking_id):
        if validate_json(new_booking):
            booking = create_booking(new_booking)
            clinic.update(booking_id, booking)
            return jsonify(booking.info())
    
    return jsonify({"error": "booking not found"}), 404

@app.patch('/bookings/<string:booking_id>/status')
def patch_status(booking_id: str):
    new_status = request.get_json()
    if "status" not in new_status:
        return jsonify({"errore: campoi mancanti"})
    
    if clinic.get(booking_id):
        clinic.get(booking_id).status = new_status["status"]
        return jsonify(clinic.get(booking_id).info())
    
@app.delete('/bookings/<string:booking_id>')
def delete_booking(booking_id: str):
    if clinic.delete(booking_id):
        return jsonify({"deleted": True, "booking_id": booking_id}), 200
    return jsonify({"error": "booking not found"}), 404 
    


    

    

    

