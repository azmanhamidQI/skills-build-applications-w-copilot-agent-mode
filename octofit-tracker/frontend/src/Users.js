import React from 'react';

function Users() {
  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Users</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Username</th>
              <th>Email</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>JohnDoe</td>
              <td>john@example.com</td>
            </tr>
            <tr>
              <td>JaneSmith</td>
              <td>jane@example.com</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Users;