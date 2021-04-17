import React, { Component } from "react";
import LineChartTimeStream from "./linechart_time_stream.js";
class DashboardStudyKing extends Component {
  state = {
    data: [
      ["08:00", "12:00"],
      ["12:30", "12:40"],
      //[13, 14],
      //[15.5, 15.8],
      //[16, 18],
      //[20, 23],
    ],
  };
  render() {
    return (
      <div id="today_study_king_display" className="mt-5 mb-5">
        <h3 style={{ fontSize: "150%" }}>Today's study king:</h3>
        <br />
        <p style={{ fontSize: "120%" }}>
          <b> 🔥 some_user</b> (with some_time)
        </p>
        <div className="text-center">
          <LineChartTimeStream data={this.state.data} />
        </div>
      </div>
    );
  }
}

export default DashboardStudyKing;