import React from 'react';

function Workouts() {
  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Workouts</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Workout</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Running</td>
              <td>Cardio exercise</td>
            </tr>
            <tr>
              <td>Swimming</td>
              <td>Full-body workout</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;