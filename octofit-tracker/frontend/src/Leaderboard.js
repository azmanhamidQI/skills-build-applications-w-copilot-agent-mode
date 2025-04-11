import React from 'react';

function Leaderboard() {
  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Leaderboard</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Username</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>JohnDoe</td>
              <td>100</td>
            </tr>
            <tr>
              <td>JaneSmith</td>
              <td>95</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;