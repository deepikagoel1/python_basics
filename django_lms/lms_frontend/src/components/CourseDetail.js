import { useParams } from "react-router-dom";
import {Link} from 'react-router-dom';

function CourseDetail() {
  let { course_id } = useParams();
  return (
    <div className="card text-right">
      <div className="row g-0">
        <div className="col-md-4">
          <img
            src="/logo512.png"
            className="img-fluid img-thumbnail"
            alt="Course Image"
          />
        </div>
        <div className="col-md-8">
          <div className="card-body">
            <h5 className="card-title">Course Title</h5>
            <p className="card-text">
              Using a combination of grid and utility classes, cards can be made
              horizontal in a mobile-friendly and responsive way. In the example
              below, we remove the grid gutters with .g-0 and use .col-md-*
              classes to make the card horizontal at the md breakpoint. Further
              adjustments may be needed depending on your card content.
            </p>
            <p className="card-text">
              <small className="text-muted">
                Course By: <a href="#">Teacher 1</a>
              </small>
            </p>
            <p className="card-text">
              <small className="text-muted">
                Duration (in hours): 3 hrs 30 minutes
              </small>
            </p>
            <p className="card-text">
              <small className="text-muted">Total Students Enrolled: 500</small>
            </p>
            <p className="card-text">
              <small className="text-muted">Rating: 4.5/5</small>
            </p>
          </div>
        </div>
      </div>
      {/*Course Video */}
      <div className="card mt-4">
        <div className="card-header">Course Videos</div>
        <ul className="list-group list-group-flush">
          <li className="list-group-item">
            Introduction
            <button
              className="btn btn-sm btn-danger float-end"
              style={{ color: "cornflowerblue" }}
            >
              <i class="bi-youtube"></i>
            </button>
          </li>
          <li className="list-group-item">
            Setup Project
            <button
              className="btn btn-sm btn-danger float-end"
              style={{ color: "cornflowerblue" }}
            >
              <i class="bi-youtube"></i>
            </button>
          </li>
          <li className="list-group-item">
            Start with functional component
            <button
              className="btn btn-sm btn-danger float-end"
              style={{ color: "cornflowerblue" }}
            >
              <i class="bi-youtube"></i>
            </button>
          </li>
          <li className="list-group-item">
            Introduction
            <button
              className="btn btn-sm btn-danger float-end"
              style={{ color: "cornflowerblue" }}
            >
              <i class="bi-youtube"></i>
            </button>
          </li>
          <li className="list-group-item">
            Setup Project
            <button
              className="btn btn-sm btn-danger float-end"
              style={{ color: "cornflowerblue" }}
            >
              <i class="bi-youtube"></i>
            </button>
          </li>
          <li className="list-group-item">
            Start with functional component
            <button
              className="btn btn-sm btn-danger float-end"
              style={{ color: "cornflowerblue" }}
            >
              <i class="bi-youtube"></i>
            </button>
          </li>
        </ul>
      </div>
      {/* End Course Video */}

      <h3 className="pb-1 mb-4 mt-5">
        Related Courses
        <a href="#" className="float-end">
          See All
        </a>{" "}
      </h3>
      <div className="row mb-4">
        <div className="col-md-3">
          <div
            className="card"
            style={{
              width: "18rem",
              fontSize: "20px",
              padding: "20px",
              backgroundColor: "light",
              color: "white",
            }}
          >
            <a href="#">
              <img src="/logo512.png" className="card-img-top" alt="..." />
            </a>
            <div className="card-body">
              <h5 className="card-title">
                <Link to="/detail/1">Course Title</Link>
              </h5>
            </div>
          </div>
        </div>

        <div className="col-md-3">
          <div
            className="card"
            style={{
              width: "18rem",
              fontSize: "20px",
              padding: "20px",
              backgroundColor: "light",
              color: "white",
            }}
          >
            <a href="#">
              <img src="/logo512.png" className="card-img-top" alt="..." />
            </a>
            <div className="card-body">
              <h5 className="card-title">
                <a href="#">Course Title</a>
              </h5>
            </div>
          </div>
        </div>

        <div className="col-md-3">
          <div
            className="card"
            style={{
              width: "18rem",
              fontSize: "20px",
              padding: "20px",
              backgroundColor: "light",
              color: "white",
            }}
          >
            <a href="#">
              <img src="/logo512.png" className="card-img-top" alt="..." />
            </a>
            <div className="card-body">
              <h5 className="card-title">
                <a href="#">Course Title</a>
              </h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default CourseDetail;
