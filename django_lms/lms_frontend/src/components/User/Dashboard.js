import {Link} from 'react-router-dom';

function Dashboard()
{
    return(
        
        <div className="container mt-4">
            <div className="row">
                 <aside className='col-md-3'>
                 <div className="card" style={{"width": "18rem"}}>
                    <h5 className='card-header'>Dashboard</h5>
                    <ul className="list-group list-group-flush">
                        <div className="list-group-item">
                        <Link to="/" className='list-group-item list-group-item-action'> My Courses</Link>
                        
                        
                        <Link to="/" className='list-group-item list-group-item-action'> Favorite Courses</Link>
                        
                        
                        <Link to="/" className='list-group-item list-group-item-action'> Recommended Courses</Link>
                        
                        
                        <Link to="/" className='list-group-item list-group-item-action'> Profile Settings</Link>
                        
                        
                        <Link to="/" className='list-group-item list-group-item-action'> Change Password</Link>
                        
                        <Link to="/" className='list-group-item list-group-item-action'> Logout</Link>
                        </div>
                    </ul>
                    </div>
                 </aside>
                 <section className='col-md-9'>
                 <div className='card mt-4'>
                    <h5 className='card-header'>My Courses</h5>
                    <div className='card-body'>
                        <table  className='table table-striped table-hover table-bordered border-primary table-primary' style={{"table-cell-padding-y": ".25rem"}}>
                            <thead>
                                <tr className='table-secondary'>
                                    <th>Name</th>
                                    <th>Created By</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <td>Php Development</td>
                                <td><Link to="/">Deepika Goel</Link></td>
                                <td>
                                    <button className='btn btn-primary'>Delete</button>
                                </td>
                            </tbody>
                        </table>
                    </div>
                 </div>
                 </section>
            </div>
        </div>
    )
}

export default Dashboard;