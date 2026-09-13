import { useEffect, useState } from "react";

import {
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import "./App.css";


function App() {

  // --------------------------------------------------
  // State
  // --------------------------------------------------

  const [currentCost, setCurrentCost] = useState(null);

  const [services, setServices] = useState([]);

  const [history, setHistory] = useState([]);

  const [anomalies, setAnomalies] = useState(null);

  const [forecast, setForecast] = useState(null);

  const [recommendations, setRecommendations] = useState(null);


  // --------------------------------------------------
  // Fetch AWS data
  // --------------------------------------------------

  useEffect(() => {

    // -----------------------------------------------
    // Current month cost
    // -----------------------------------------------

    fetch("/api/costs/current")
      .then((response) => response.json())
      .then((data) => {
        setCurrentCost(data);
      })
      .catch((error) => {
        console.error("Current cost error:", error);
      });


    // -----------------------------------------------
    // Cost by AWS service
    // -----------------------------------------------

    fetch("/api/costs/services")
      .then((response) => response.json())
      .then((data) => {
        setServices(data);
      })
      .catch((error) => {
        console.error("Service cost error:", error);
      });


    // -----------------------------------------------
    // Daily cost history
    // -----------------------------------------------

    fetch("/api/costs/history?days=7")
      .then((response) => response.json())
      .then((data) => {
        setHistory(data);
      })
      .catch((error) => {
        console.error("History error:", error);
      });


    // -----------------------------------------------
    // Cost anomaly detection
    // -----------------------------------------------

    fetch("/api/anomalies?days=30")
      .then((response) => response.json())
      .then((data) => {
        setAnomalies(data);
      })
      .catch((error) => {
        console.error("Anomaly error:", error);
      });


    // -----------------------------------------------
    // Cost forecast
    // -----------------------------------------------

    fetch("/api/costs/forecast")
      .then((response) => response.json())
      .then((data) => {
        setForecast(data);
      })
      .catch((error) => {
        console.error("Forecast error:", error);
      });


    // -----------------------------------------------
    // Cost optimization recommendations
    // -----------------------------------------------

    fetch("/api/optimization/recommendations")
      .then((response) => response.json())
      .then((data) => {
        setRecommendations(data);
      })
      .catch((error) => {
        console.error("Recommendation error:", error);
      });

  }, []);


  // --------------------------------------------------
  // Render
  // --------------------------------------------------

  return (

    <div className="dashboard">


      {/* ==========================================
          HEADER
      ========================================== */}

      <header className="header">

        <div>

          <h1>
            Cloud Cost Optimizer
          </h1>

          <p>
            AWS Cloud Cost Monitoring Platform
          </p>

        </div>


        <div className="status">

          <span className="status-dot"></span>

          AWS Connected

        </div>

      </header>


      {/* ==========================================
          SUMMARY CARDS
      ========================================== */}

      <section className="cards">


        {/* ----------------------------------------
            Current Cost
        ---------------------------------------- */}

        <div className="card">

          <p>
            Current Month Cost
          </p>

          <h2>

            {currentCost
              ? `$${currentCost.cost.toFixed(2)}`
              : "Loading..."}

          </h2>

          <span className="card-description">

            Current AWS spending

          </span>

        </div>


        {/* ----------------------------------------
            AWS Services
        ---------------------------------------- */}

        <div className="card">

          <p>
            AWS Services
          </p>

          <h2>

            {services.length}

          </h2>

          <span className="card-description">

            Services with usage

          </span>

        </div>


        {/* ----------------------------------------
            Cost Anomalies
        ---------------------------------------- */}

        <div className="card">

          <p>
            Cost Anomalies
          </p>

          <h2>

            {anomalies
              ? anomalies.anomalies.length
              : "Loading..."}

          </h2>

          <span className="card-description">

            {anomalies &&
            anomalies.anomalies.length === 0
              ? "No unusual spending detected"
              : "Unusual spending detected"}

          </span>

        </div>


        {/* ----------------------------------------
            Month-End Forecast
        ---------------------------------------- */}

        <div className="card">

          <p>
            Estimated Month-End Cost
          </p>

          <h2>

            {forecast
              ? `$${forecast.estimated_month_end_cost.toFixed(2)}`
              : "Loading..."}

          </h2>

          <span className="card-description">

            Based on current daily spending

          </span>

        </div>

      </section>


      {/* ==========================================
          FORECAST DETAILS
      ========================================== */}

      {forecast && (

        <section className="panel">

          <div className="panel-header">

            <div>

              <h2>
                Cost Forecast
              </h2>

              <p>
                Estimated AWS spending for the current month
              </p>

            </div>

          </div>


          <div className="cards">


            {/* Current Spending */}

            <div className="card">

              <p>
                Current Spending
              </p>

              <h2>
                ${forecast.current_cost.toFixed(2)}
              </h2>

              <span className="card-description">
                Spending so far this month
              </span>

            </div>


            {/* Average Daily Cost */}

            <div className="card">

              <p>
                Average Daily Cost
              </p>

              <h2>
                ${forecast.average_daily_cost.toFixed(2)}
              </h2>

              <span className="card-description">
                Average AWS spending per day
              </span>

            </div>


            {/* Days Remaining */}

            <div className="card">

              <p>
                Days Remaining
              </p>

              <h2>
                {forecast.days_remaining}
              </h2>

              <span className="card-description">
                Remaining days in this month
              </span>

            </div>


            {/* Remaining Forecast */}

            <div className="card">

              <p>
                Expected Remaining Cost
              </p>

              <h2>
                ${forecast.remaining_forecast.toFixed(2)}
              </h2>

              <span className="card-description">
                Projected additional spending
              </span>

            </div>

          </div>


          {/* Forecast Explanation */}

          <div className="normal-panel">

            <h3>
              Forecast Method
            </h3>

            <p>

              The estimated month-end cost is calculated using
              the current average daily AWS spending.

            </p>

            <p>

              Current spending:

              <strong>
                {" "}
                ${forecast.current_cost.toFixed(2)}
              </strong>

            </p>

            <p>

              Average daily spending:

              <strong>
                {" "}
                ${forecast.average_daily_cost.toFixed(2)}
              </strong>

            </p>

            <p>

              Estimated month-end spending:

              <strong>
                {" "}
                ${forecast.estimated_month_end_cost.toFixed(2)}
              </strong>

            </p>

          </div>

        </section>

      )}


      {/* ==========================================
          COST OPTIMIZATION RECOMMENDATIONS
      ========================================== */}

      {recommendations && (

        <section className="panel">

          <div className="panel-header">

            <div>

              <h2>
                Cost Optimization Recommendations
              </h2>

              <p>
                AWS cost-saving recommendations based on
                current service spending
              </p>

            </div>

          </div>


          {recommendations.recommendations.length > 0 ? (

            <div className="recommendations">

              {recommendations.recommendations.map((item) => (

                <div
                  className="recommendation"
                  key={item.service}
                >

                  <div className="recommendation-header">

                    <div>

                      <h3>
                        {item.service}
                      </h3>

                      <p className="recommendation-cost">
                        Current Cost: ${Number(item.cost).toFixed(2)}
                      </p>

                    </div>


                    <span
                      className={`priority priority-${item.priority}`}
                    >
                      {item.priority.toUpperCase()}
                    </span>

                  </div>


                  <div className="recommendation-message">

                    <strong>
                      Recommendation
                    </strong>

                    <p>
                      {item.recommendation}
                    </p>

                  </div>

                </div>

              ))}

            </div>

          ) : (

            <div className="normal-panel">

              <h3>
                No Recommendations
              </h3>

              <p>
                No AWS service cost data is currently available
                for optimization recommendations.
              </p>

            </div>

          )}

        </section>

      )}


      {/* ==========================================
          ANOMALY ALERT
      ========================================== */}

      {anomalies &&
        anomalies.anomalies.length > 0 && (

          <section className="panel anomaly-panel">

            <div className="panel-header">

              <div>

                <h2>
                  Cost Anomalies Detected
                </h2>

                <p>
                  Unusual AWS spending was detected
                </p>

              </div>

            </div>


            {anomalies.anomalies.map((anomaly) => (

              <div
                className="anomaly"
                key={anomaly.date}
              >

                <div>

                  <strong>
                    🚨 {anomaly.date}
                  </strong>

                  <p>
                    {anomaly.message}
                  </p>

                </div>


                <div className="anomaly-details">

                  <span>

                    Cost:

                    <strong>
                      ${anomaly.cost.toFixed(2)}
                    </strong>

                  </span>


                  <span>

                    Average:

                    <strong>
                      ${anomaly.average_cost.toFixed(2)}
                    </strong>

                  </span>


                  <span>

                    Increase:

                    <strong>
                      {anomaly.increase_percentage.toFixed(2)}%
                    </strong>

                  </span>

                </div>

              </div>

            ))}

          </section>

        )}


      {/* ==========================================
          NORMAL COST STATUS
      ========================================== */}

      {anomalies &&
        anomalies.status === "normal" && (

          <section className="panel normal-panel">

            <h2>
              Cost Status
            </h2>

            <p>
              ✅ No unusual AWS spending detected.
            </p>

            <p>

              Average daily cost:

              <strong>
                {" "}
                ${anomalies.average_daily_cost.toFixed(2)}
              </strong>

            </p>

          </section>

        )}


      {/* ==========================================
          DAILY COST TREND
      ========================================== */}

      <section className="panel">

        <div className="panel-header">

          <div>

            <h2>
              Daily Cost Trend
            </h2>

            <p>
              AWS spending over the last 7 days
            </p>

          </div>

        </div>


        <div className="chart">

          {history.length > 0 ? (

            <ResponsiveContainer
              width="100%"
              height={350}
            >

              <LineChart data={history}>

                <CartesianGrid
                  strokeDasharray="3 3"
                />

                <XAxis
                  dataKey="date"
                />

                <YAxis />

                <Tooltip />

                <Line
                  type="monotone"
                  dataKey="cost"
                  strokeWidth={3}
                />

              </LineChart>

            </ResponsiveContainer>

          ) : (

            <p>
              Loading cost history...
            </p>

          )}

        </div>

      </section>


      {/* ==========================================
          COST BY AWS SERVICE
      ========================================== */}

      <section className="panel">

        <div className="panel-header">

          <div>

            <h2>
              Cost by AWS Service
            </h2>

            <p>
              Monthly spending by AWS service
            </p>

          </div>

        </div>


        <div className="chart">

          {services.length > 0 ? (

            <ResponsiveContainer
              width="100%"
              height={400}
            >

              <BarChart
                data={services.slice(0, 10)}
                layout="vertical"
                margin={{
                  left: 40,
                  right: 30,
                }}
              >

                <CartesianGrid
                  strokeDasharray="3 3"
                />

                <XAxis
                  type="number"
                />

                <YAxis
                  type="category"
                  dataKey="service"
                  width={250}
                />

                <Tooltip />

                <Bar
                  dataKey="cost"
                  barSize={25}
                />

              </BarChart>

            </ResponsiveContainer>

          ) : (

            <p>
              Loading service costs...
            </p>

          )}

        </div>

      </section>


      {/* ==========================================
          SERVICE BREAKDOWN
      ========================================== */}

      <section className="panel">

        <div className="panel-header">

          <div>

            <h2>
              Service Breakdown
            </h2>

            <p>
              Detailed AWS cost information
            </p>

          </div>

        </div>


        {services.length > 0 ? (

          <table>

            <thead>

              <tr>

                <th>
                  AWS Service
                </th>

                <th>
                  Cost
                </th>

                <th>
                  Currency
                </th>

              </tr>

            </thead>


            <tbody>

              {services.map((item) => (

                <tr
                  key={item.service}
                >

                  <td>
                    {item.service}
                  </td>

                  <td>
                    ${item.cost.toFixed(2)}
                  </td>

                  <td>
                    {item.currency}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        ) : (

          <p>
            Loading service information...
          </p>

        )}

      </section>


      {/* ==========================================
          FOOTER
      ========================================== */}

      <footer>

        <p>
          Cloud Cost Optimizer • AWS Cost Monitoring
        </p>

      </footer>


    </div>

  );
}


export default App;