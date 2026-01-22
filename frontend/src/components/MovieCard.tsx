import React from 'react';
import { Movie } from '../types';
import { Calendar, Users, Tag, Star, Play, Sparkles } from 'lucide-react';

interface MovieCardProps {
  movie: Movie;
  onClick: () => void;
}

export const MovieCard: React.FC<MovieCardProps> = ({ movie, onClick }) => {
  return (
    <div 
      className="group relative bg-gradient-to-br from-gray-900/70 via-gray-800/50 to-gray-900/70 backdrop-blur-xl rounded-3xl overflow-hidden cursor-pointer transform transition-all duration-500 hover:scale-[1.02] hover:-translate-y-2 border border-gray-700/30 hover:border-purple-500/40 shadow-2xl hover:shadow-purple-500/20"
      onClick={onClick}
      style={{
        background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(30, 41, 59, 0.6) 50%, rgba(15, 23, 42, 0.8) 100%)',
      }}
    >
      {/* Poster */}
      <div className="relative aspect-[2/3] overflow-hidden">
        {movie.poster_url ? (
          <img 
            src={movie.poster_url} 
            alt={movie.title}
            className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
          />
        ) : (
          <div className="w-full h-full bg-gradient-to-br from-gray-800 to-gray-900 flex items-center justify-center">
            <div className="text-gray-400 text-center">
              <Tag className="w-12 h-12 mx-auto mb-2 opacity-50" />
              <p className="text-sm">No poster</p>
            </div>
          </div>
        )}
        
        {/* Magical Shimmer Effect */}
        <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent opacity-0 group-hover:opacity-100 transform -skew-x-12 translate-x-[-200%] group-hover:translate-x-[200%] transition-all duration-1000 ease-out"></div>
        
        {/* Overlay */}
        <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500">
          {/* Play button */}
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="relative bg-gradient-to-r from-red-600 to-pink-600 backdrop-blur-sm p-5 rounded-full transform translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-500 shadow-2xl shadow-red-500/30">
              <Play className="w-7 h-7 text-white fill-white transform group-hover:scale-110 transition-transform duration-300" />
              <div className="absolute inset-0 rounded-full bg-gradient-to-r from-red-400 to-pink-400 animate-ping opacity-30"></div>
            </div>
          </div>
          
          {/* Rating */}
          <div className="absolute top-4 left-4 flex items-center space-x-2 bg-gradient-to-r from-yellow-500/20 to-orange-500/20 backdrop-blur-xl px-4 py-2 rounded-full border border-yellow-400/30 shadow-lg">
            <Star className="w-4 h-4 fill-yellow-400 text-yellow-400 animate-pulse" />
            <span className="text-white text-sm font-bold">8.5</span>
          </div>
          
          {/* Year */}
          {movie.release_year && (
            <div className="absolute top-4 right-4 bg-gradient-to-r from-purple-500/20 to-blue-500/20 backdrop-blur-xl px-4 py-2 rounded-full border border-purple-400/30 shadow-lg">
              <span className="text-white text-sm font-bold">{movie.release_year}</span>
            </div>
          )}
          
          {/* Sparkle Effect */}
          <div className="absolute top-6 right-6 opacity-0 group-hover:opacity-100 transition-opacity duration-700 delay-300">
            <Sparkles className="w-5 h-5 text-yellow-300 animate-bounce" />
          </div>
        </div>
      </div>
      
      {/* Content */}
      <div className="p-6 relative">
        {/* Gradient Border Effect */}
        <div className="absolute top-0 left-4 right-4 h-px bg-gradient-to-r from-transparent via-purple-400/30 to-transparent"></div>
        
        <h3 className="text-white font-bold text-xl mb-4 line-clamp-2 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-white group-hover:to-purple-200 group-hover:bg-clip-text transition-all duration-300 leading-tight">
          {movie.title}
        </h3>
        
        {/* Genres */}
        {movie.genres.length > 0 && (
          <div className="flex flex-wrap gap-2 mb-4">
            {movie.genres.slice(0, 2).map((genre, index) => (
              <span
                key={genre.id}
                className={`px-3 py-1.5 text-xs font-semibold rounded-full border transition-all duration-300 ${
                  index === 0 
                    ? 'bg-gradient-to-r from-purple-500/20 to-blue-500/20 border-purple-400/40 text-purple-200 group-hover:from-purple-400/30 group-hover:to-blue-400/30' 
                    : 'bg-gradient-to-r from-pink-500/20 to-red-500/20 border-pink-400/40 text-pink-200 group-hover:from-pink-400/30 group-hover:to-red-400/30'
                }`}
              >
                {genre.name}
              </span>
            ))}
            {movie.genres.length > 2 && (
              <span className="px-3 py-1.5 bg-gradient-to-r from-gray-600/30 to-gray-500/30 border border-gray-500/40 text-gray-300 rounded-full text-xs font-semibold">
                +{movie.genres.length - 2}
              </span>
            )}
          </div>
        )}
        
        {/* Director */}
        {movie.director && (
          <div className="flex items-center text-gray-300 text-sm mb-3 group-hover:text-gray-200 transition-colors duration-300">
            <div className="flex items-center justify-center w-6 h-6 rounded-full bg-gradient-to-r from-blue-500/20 to-purple-500/20 border border-blue-400/30 mr-3">
              <Users className="w-3 h-3 text-blue-300" />
            </div>
            <span className="truncate font-medium">{movie.director.name}</span>
          </div>
        )}
        
        {/* Description */}
        {movie.description && (
          <p className="text-gray-400 text-sm leading-relaxed line-clamp-2 group-hover:text-gray-300 transition-colors duration-300">
            {movie.description}
          </p>
        )}
        
        {/* Bottom Glow Effect */}
        <div className="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-purple-400/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
      </div>
    </div>
  );
};
