// function DataTable({data}){
//   return (
//     <>
//       <table>
//         <thead>
//           <tr>
//             <th>Time</th>
//             <th>Distance</th>
//             <th>Flow</th>
//             <th>Status</th>
//           </tr>
//         </thead>
//         <tbody>
//           {data.map((item, index) => (
//             <tr key={index}>
//               <td>{new Date(item.timestamp).toLocaleString()}</td>
//               <td>{item.distance}</td>
//               <td>{item.flow}</td>
//               <td style={{
//                 color:
//                   item.status === "danger" ? "red" :
//                   item.status === "warning" ? "orange" : "green"
//               }}>
//                 {item.status}
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </>
//   )
// }
//
// export default DataTable

import React from "react";

const DataTable = ({ data }) => {
  return (
    <div className="table-container">
      <h3>Recent Data</h3>

      <table>
        <thead>
          <tr>
            <th>Time</th>
            <th>Distance</th>
            <th>Flow</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{new Date(item.timestamp).toLocaleString()}</td>
              <td>{item.distance}</td>
              <td>{item.flow}</td>
              <td className={item.status.toLowerCase()} style={{
                color:
                  item.status === "danger" ? "red":
                  item.status === "warning" ? "orange": "green"
              }}>
                {item.status}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataTable;
