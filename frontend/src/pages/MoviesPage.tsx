import React, { useState, useEffect } from 'react';
import { Movie, Genre, Director, Actor, MovieFilters } from '../types';
import { movieApi, genreApi, directorApi, actorApi } from '../services/api';
import { MovieCard } from '../components/MovieCard';
import { MovieFiltersComponent } from '../components/MovieFilters';
import { useNavigate } from 'react-router-dom';

export const MoviesPage: React.FC = () => {
  const [movies, setMovies] = useState<Movie[]>([]);
  const [genres, setGenres] = useState<Genre[]>([]);
  const [directors, setDirectors] = useState<Director[]>([]);
  const [actors, setActors] = useState<Actor[]>([]);
  const [filters, setFilters] = useState<MovieFilters>({});
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    loadInitialData();
  }, []);

  useEffect(() => {
    loadMovies();
  }, [filters]);

  const loadInitialData = async () => {
    try {
      const [genresData, directorsData, actorsData] = await Promise.all([
        genreApi.getGenres(),
        directorApi.getDirectors(),
        actorApi.getActors()
      ]);
      setGenres(genresData);
      setDirectors(directorsData);
      setActors(actorsData);
    } catch (error) {
      console.error('Failed to load initial data:', error);
    }
  };

  const loadMovies = async () => {
    setLoading(true);
    try {
      const moviesData = await movieApi.getMovies(filters);
      setMovies(moviesData);
    } catch (error) {
      console.error('Failed to load movies:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleMovieClick = (movie: Movie) => {
    navigate(`/movies/${movie.id}`);
  };

  return (
    <div className="min-h-screen relative overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-purple-900/20 via-transparent to-transparent animate-pulse"></div>
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl animate-float"></div>
        <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl animate-float-delay"></div>
      </div>
      
      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Hero Header */}
        <div className="mb-16 text-center relative">
          {/* Floating particles */}
          <div className="absolute inset-0 overflow-hidden pointer-events-none">
            <div className="absolute top-10 left-1/4 w-2 h-2 bg-purple-400 rounded-full animate-ping opacity-60"></div>
            <div className="absolute top-20 right-1/3 w-1 h-1 bg-blue-400 rounded-full animate-pulse opacity-40"></div>
            <div className="absolute top-32 left-1/2 w-1.5 h-1.5 bg-pink-400 rounded-full animate-bounce opacity-50"></div>
          </div>
          
          <div className="relative">
            <h1 className="text-5xl md:text-6xl font-black mb-6 tracking-tight">
              <span className="bg-gradient-to-r from-white via-purple-200 via-pink-200 to-white bg-clip-text text-transparent animate-gradient-x bg-300% leading-none block">
                Movie Explorer
              </span>
            </h1>
            
            {/* Glowing underline */}
            <div className="w-32 h-1 bg-gradient-to-r from-purple-500 to-pink-500 mx-auto mb-8 rounded-full shadow-lg shadow-purple-500/50 animate-pulse"></div>
            
            <p className="text-xl md:text-2xl text-gray-300 max-w-3xl mx-auto leading-relaxed font-light">
              Discover your next favorite movie from our collection of{' '}
              <span className="font-bold text-transparent bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text animate-pulse">
                {movies.length} films
              </span>{' '}
              across all genres
            </p>
          </div>
        </div>

        <MovieFiltersComponent
          filters={filters}
          genres={genres}
          directors={directors}
          actors={actors}
          onFiltersChange={setFilters}
        />

        {loading ? (
          <div className="flex justify-center items-center py-32">
            <div className="relative">
              {/* Main loader */}
              <div className="animate-spin rounded-full h-20 w-20 border-4 border-transparent border-t-purple-500 border-r-pink-500 shadow-2xl"></div>
              
              {/* Inner loader */}
              <div className="absolute inset-2 animate-spin rounded-full border-4 border-transparent border-t-blue-400 border-l-purple-400 animate-reverse-spin"></div>
              
              {/* Pulsing background */}
              <div className="absolute inset-0 animate-ping rounded-full border-4 border-purple-300/30"></div>
              
              {/* Floating dots */}
              <div className="absolute -top-2 -left-2 w-2 h-2 bg-purple-400 rounded-full animate-bounce"></div>
              <div className="absolute -top-2 -right-2 w-2 h-2 bg-pink-400 rounded-full animate-bounce delay-150"></div>
              <div className="absolute -bottom-2 -left-2 w-2 h-2 bg-blue-400 rounded-full animate-bounce delay-300"></div>
              <div className="absolute -bottom-2 -right-2 w-2 h-2 bg-purple-400 rounded-full animate-bounce delay-500"></div>
            </div>
            <div className="ml-6">
              <p className="text-white text-xl font-semibold animate-pulse">Loading Movies</p>
              <p className="text-gray-400 text-sm">Please wait while we fetch the latest collection...</p>
            </div>
          </div>
        ) : (
          <>
            <div className="mb-8 flex items-center justify-between">
              <div className="flex items-center space-x-4">
                <h2 className="text-2xl font-bold text-white">
                  {movies.length} movie{movies.length !== 1 ? 's' : ''} found
                </h2>
                {Object.keys(filters).length > 0 && (
                  <button
                    onClick={() => setFilters({})}
                    className="px-4 py-2 bg-red-600/20 hover:bg-red-600/30 text-red-300 hover:text-red-200 border border-red-500/30 rounded-lg text-sm font-medium transition-colors duration-200"
                  >
                    Clear Filters
                  </button>
                )}
              </div>
            </div>

            {movies.length === 0 ? (
              <div className="text-center py-20">
                <div className="max-w-md mx-auto">
                  <div className="w-24 h-24 mx-auto mb-6 rounded-full bg-gradient-to-br from-purple-500/20 to-blue-500/20 flex items-center justify-center">
                    <svg className="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <p className="text-gray-300 text-xl font-semibold mb-2">No movies found</p>
                  <p className="text-gray-400">Try adjusting your search criteria or filters to discover more movies</p>
                </div>
              </div>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 gap-6">
                {movies.map((movie) => (
                  <MovieCard
                    key={movie.id}
                    movie={movie}
                    onClick={() => handleMovieClick(movie)}
                  />
                ))}
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
};
