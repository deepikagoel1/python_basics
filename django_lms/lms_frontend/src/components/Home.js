import {Link} from 'react-router-dom';

function Home() {
  return (
    <div className="container mt-4">
        {/* Latest Courses */}
        <h3 className="pb-1 mb-4">Latest Courses <a href="#" className="float-end">See All</a> </h3> 
        <div className="row">
            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white'
                            
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><Link to="/detail/1">Course Title</Link></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Course Title</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Course Title</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Course Title</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3 mt-5">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Course Title</a></h5>
                    </div>
                </div>
            </div>

        </div>
        {/* End Latest Courses */}
        {/* Popular Courses */}
        <h3 className="pb-1 mb-4 mt-5">Popular Courses <a href="#" className="float-end">See All</a> </h3> 
        <div className="row">
            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white'
                            
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Course Title</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Course Title</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Course Title</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Course Title</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3 mt-5">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Course Title</a></h5>
                    </div>
                </div>
            </div>

        </div>
        {/* End Popular Courses */}

        {/* Popular Teachers */}
        <h3 className="pb-1 mb-4 mt-5">Featured Teachers <a href="#" className="float-end">See All</a> </h3> 
        <div className="row">
            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white'
                            
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Teacher Name</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Teacher Name</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Teacher Name</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Teacher Name</a></h5>
                    </div>
                </div>
            </div>

            <div className="col-md-3 mt-5">
                <div className="card" style={{
                            width: '18rem',
                            fontSize: '20px',
                            padding: '20px',
                            backgroundColor: 'light',
                            color: 'white',
                            }}>
                        <a href="#"><img src="logo512.png" className="card-img-top" alt="..."/></a>
                    <div className="card-body">
                    <h5 className="card-title"><a href="#">Teacher Name</a></h5>
                    </div>
                </div>
            </div>

        </div>
        {/* End Popular Teachers */}

        {/* Student Testimonial */}
        <h3 className="pb-1 mb-4 mt-5"> Student Testimonial</h3> 
        <div id="carouselExampleIndicators" class="carousel slide bg-dark text-light py-3" data-bs-ride="carousel">
            <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
            </div>
            <div class="carousel-inner">
                <div class="carousel-item active">
                <figure class="text-center">
                <blockquote class="blockquote">
                    <p>A well-known quote, contained in a blockquote element.</p>
                </blockquote>
                <figcaption class="blockquote-footer">
                    Someone famous in <cite title="Source Title">Source Title</cite>
                </figcaption>
                </figure>
                </div>
                <div class="carousel-item">
                <figure class="text-center">
                <blockquote class="blockquote">
                    <p>A well-known quote, contained in a blockquote element.</p>
                </blockquote>
                <figcaption class="blockquote-footer">
                    Someone famous in <cite title="Source Title">Source Title</cite>
                </figcaption>
                </figure>
                </div>
                <div class="carousel-item">
                <figure class="text-center">
                <blockquote class="blockquote">
                    <p>A well-known quote, contained in a blockquote element.</p>
                </blockquote>
                <figcaption class="blockquote-footer">
                    Someone famous in <cite title="Source Title">Source Title</cite>
                </figcaption>
                </figure>
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
            </div>
        {/* End Student Testimonial */}


      </div>
  );
}

export default Home;
