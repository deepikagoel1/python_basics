import Header from './Header';
import Home from './Home';
import About from './About';
import Footer from './Footer';
import CourseDetail from './CourseDetail'
import {Routes as Switch, Route} from 'react-router-dom';
import Login from './User/Login';
import Register from './User/Register';

function Main() {
  return (
    <div className="App">
        
      <Header />
      <Switch>
        <Route path = "/" element = {<Home />} />
        <Route path = "/about" element = {<About />} />
        <Route path = "/detail/:course_id" element = {<CourseDetail />} />
        <Route path = "/login" element = {<Login />} />
        <Route path = "/register" element = {<Register />} />
      </Switch>
      <Footer />
      
      
    </div>
  );
}

export default Main;