import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { MoviesPage } from './pages/MoviesPage';
import { MovieDetailPage } from './pages/MovieDetailPage';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<MoviesPage />} />
          <Route path="/movies/:id" element={<MovieDetailPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
