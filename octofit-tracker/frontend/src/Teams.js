import React from 'react';

function Teams() {
  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Teams</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Team Name</th>
              <th>Members</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Team Alpha</td>
              <td>John, Jane</td>
            </tr>
            <tr>
              <td>Team Beta</td>
              <td>Mike, Sarah</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Teams;