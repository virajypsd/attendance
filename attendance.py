from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load attendance data
def load_attendance():
    try:
        df = pd.read_csv("attendance.csv")
        return df.to_dict(orient="records")  # Convert to JSON
    except:
        return []

@app.route("/attendance", methods=["GET"])
def get_attendance():
    """Return attendance data as JSON"""
    data = load_attendance()
    return jsonify(data)

@app.route("/update_attendance", methods=["POST"])
def update_attendance():
    """Receive new attendance data"""
    try:
        new_data = request.json
        df = pd.DataFrame(new_data)
        df.to_csv("attendance.csv", index=False, mode="a", header=False)
        return jsonify({"message": "Attendance updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

