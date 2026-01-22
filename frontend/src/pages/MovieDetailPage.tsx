import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Movie } from '../types';
import { movieApi } from '../services/api';
import { Calendar, Users, Tag, ArrowLeft, Star, Play, Heart, Share2 } from 'lucide-react';

export const MovieDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [movie, setMovie] = useState<Movie | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (id) {
      loadMovie(parseInt(id));
    }
  }, [id]);

  const loadMovie = async (movieId: number) => {
    setLoading(true);
    try {
      const movieData = await movieApi.getMovie(movieId);
      setMovie(movieData);
    } catch (error) {
      console.error('Failed to load movie:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex justify-center items-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (!movie) {
    return (
      <div className="min-h-screen bg-gray-50 flex justify-center items-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Movie not found</h2>
          <button
            onClick={() => navigate('/')}
            className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
          >
            Back to Movies
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Hero Section with Background */}
      <div className="relative">
        {/* Background Image Overlay */}
        <div className="absolute inset-0 overflow-hidden">
          {movie.poster_url && (
            <img
              src={movie.poster_url}
              alt={movie.title}
              className="w-full h-full object-cover opacity-20 blur-sm"
            />
          )}
          <div className="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/80 to-transparent"></div>
        </div>

        {/* Content */}
        <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {/* Back Button */}
          <button
            onClick={() => navigate('/')}
            className="flex items-center mb-8 text-white/80 hover:text-white transition-colors duration-200 group"
          >
            <ArrowLeft className="w-5 h-5 mr-2 transition-transform group-hover:-translate-x-1" />
            <span className="text-lg font-medium">Back to Movies</span>
          </button>

          <div className="grid lg:grid-cols-5 gap-12">
            {/* Movie Poster */}
            <div className="lg:col-span-2">
              <div className="relative group">
                <div className="aspect-[2/3] rounded-2xl overflow-hidden shadow-2xl ring-1 ring-white/10">
                  {movie.poster_url ? (
                    <img
                      src={movie.poster_url}
                      alt={movie.title}
                      className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                    />
                  ) : (
                    <div className="w-full h-full bg-gradient-to-br from-gray-800 to-gray-900 flex items-center justify-center">
                      <div className="text-gray-400 text-center">
                        <Tag className="w-16 h-16 mx-auto mb-4 opacity-50" />
                        <p className="text-xl">No poster available</p>
                      </div>
                    </div>
                  )}
                </div>
                
                {/* Action Buttons */}
                <div className="mt-6 flex gap-4">
                  <button className="flex-1 bg-red-600 hover:bg-red-700 text-white px-6 py-3 rounded-xl font-semibold transition-colors duration-200 flex items-center justify-center gap-2">
                    <Play className="w-5 h-5" />
                    Watch Trailer
                  </button>
                  <button className="p-3 bg-white/10 hover:bg-white/20 backdrop-blur-sm text-white rounded-xl transition-colors duration-200">
                    <Heart className="w-6 h-6" />
                  </button>
                  <button className="p-3 bg-white/10 hover:bg-white/20 backdrop-blur-sm text-white rounded-xl transition-colors duration-200">
                    <Share2 className="w-6 h-6" />
                  </button>
                </div>
              </div>
            </div>

            {/* Movie Details */}
            <div className="lg:col-span-3 text-white">
              <div className="space-y-6">
                {/* Title and Rating */}
                <div>
                  <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
                    {movie.title}
                  </h1>
                  <div className="flex items-center gap-4 text-lg">
                    <div className="flex items-center gap-1">
                      <Star className="w-5 h-5 fill-yellow-400 text-yellow-400" />
                      <span className="font-semibold">8.5</span>
                      <span className="text-gray-400">/10</span>
                    </div>
                    <span className="text-gray-400">•</span>
                    <span className="text-gray-300">{movie.release_year}</span>
                  </div>
                </div>

                {/* Genres */}
                {movie.genres.length > 0 && (
                  <div className="flex flex-wrap gap-2">
                    {movie.genres.map((genre) => (
                      <span
                        key={genre.id}
                        className="px-4 py-2 bg-white/10 backdrop-blur-sm text-white rounded-full text-sm font-medium border border-white/20 hover:bg-white/20 transition-colors duration-200"
                      >
                        {genre.name}
                      </span>
                    ))}
                  </div>
                )}

                {/* Synopsis */}
                {movie.description && (
                  <div className="space-y-3">
                    <h3 className="text-2xl font-semibold text-white">Synopsis</h3>
                    <p className="text-gray-300 leading-relaxed text-lg">{movie.description}</p>
                  </div>
                )}

                {/* Director */}
                {movie.director && (
                  <div className="space-y-3">
                    <h3 className="text-2xl font-semibold text-white">Director</h3>
                    <div className="p-4 bg-white/5 backdrop-blur-sm rounded-xl border border-white/10">
                      <p className="text-xl font-semibold text-white">{movie.director.name}</p>
                      {movie.director.bio && (
                        <p className="text-gray-300 mt-2 leading-relaxed">{movie.director.bio}</p>
                      )}
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* Cast Section */}
          {movie.actors.length > 0 && (
            <div className="mt-16">
              <h3 className="text-3xl font-bold text-white mb-8">Cast</h3>
              <div className="flex flex-wrap gap-3">
                {movie.actors.slice(0, 12).map((actor) => (
                  <div
                    key={actor.id}
                    className="px-4 py-2 bg-white/10 backdrop-blur-sm text-white rounded-full text-sm font-medium border border-white/20 hover:bg-white/20 transition-colors duration-200"
                  >
                    {actor.name}
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
