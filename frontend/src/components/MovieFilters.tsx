import React from 'react';
import { Genre, Director, Actor, MovieFilters } from '../types';
import { Search, Filter } from 'lucide-react';

interface MovieFiltersProps {
  filters: MovieFilters;
  genres: Genre[];
  directors: Director[];
  actors: Actor[];
  onFiltersChange: (filters: MovieFilters) => void;
}

export const MovieFiltersComponent: React.FC<MovieFiltersProps> = ({
  filters,
  genres,
  directors,
  actors,
  onFiltersChange,
}) => {
  const handleFilterChange = (key: keyof MovieFilters, value: string | number | undefined) => {
    const newFilters = { ...filters };
    if (value === '' || value === 0) {
      delete newFilters[key];
    } else {
      newFilters[key] = value as any;
    }
    onFiltersChange(newFilters);
  };

  return (
    <div className="relative bg-gradient-to-br from-black/30 via-purple-900/20 to-black/30 backdrop-blur-xl border border-purple-500/20 p-8 rounded-3xl mb-12 shadow-2xl shadow-purple-500/10 group hover:shadow-purple-500/20 transition-all duration-500">
      {/* Animated border glow */}
      <div className="absolute inset-0 rounded-3xl bg-gradient-to-r from-purple-500/20 via-pink-500/20 to-blue-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 -z-10 blur-xl"></div>
      
      <div className="flex items-center mb-8 relative">
        <div className="flex items-center justify-center w-10 h-10 rounded-full bg-gradient-to-r from-purple-500/20 to-pink-500/20 border border-purple-400/30 mr-4 group-hover:scale-110 transition-transform duration-300">
          <Filter className="w-5 h-5 text-purple-300 group-hover:text-purple-200 transition-colors duration-300" />
        </div>
        <h2 className="text-2xl font-bold text-transparent bg-gradient-to-r from-white via-purple-200 to-white bg-clip-text animate-gradient-x bg-300%">
          Filter & Search
        </h2>
        
        {/* Decorative elements */}
        <div className="ml-auto flex space-x-2">
          <div className="w-2 h-2 rounded-full bg-purple-400 animate-pulse opacity-60"></div>
          <div className="w-2 h-2 rounded-full bg-pink-400 animate-pulse opacity-60 delay-200"></div>
          <div className="w-2 h-2 rounded-full bg-blue-400 animate-pulse opacity-60 delay-500"></div>
        </div>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
        {/* Search */}
        <div className="lg:col-span-2">
          <label className="block text-sm font-medium text-gray-300 mb-2">
            Search Movies
          </label>
          <div className="relative">
            <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
            <input
              type="text"
              placeholder="Search by title, actor, director..."
              value={filters.search || ''}
              onChange={(e) => handleFilterChange('search', e.target.value)}
              className="pl-12 w-full px-4 py-3 bg-white/5 border border-gray-600/50 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-200"
            />
          </div>
        </div>

        {/* Genre Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-300 mb-2">
            Genre
          </label>
          <select
            value={filters.genre_id || ''}
            onChange={(e) => handleFilterChange('genre_id', e.target.value ? parseInt(e.target.value) : undefined)}
            className="w-full px-4 py-3 bg-white/5 border border-gray-600/50 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-200 appearance-none cursor-pointer"
          >
            <option value="" className="bg-gray-900 text-white">All Genres</option>
            {genres.map((genre) => (
              <option key={genre.id} value={genre.id} className="bg-gray-900 text-white">
                {genre.name}
              </option>
            ))}
          </select>
        </div>

        {/* Director Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-300 mb-2">
            Director
          </label>
          <select
            value={filters.director_id || ''}
            onChange={(e) => handleFilterChange('director_id', e.target.value ? parseInt(e.target.value) : undefined)}
            className="w-full px-4 py-3 bg-white/5 border border-gray-600/50 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-200 appearance-none cursor-pointer"
          >
            <option value="" className="bg-gray-900 text-white">All Directors</option>
            {directors.map((director) => (
              <option key={director.id} value={director.id} className="bg-gray-900 text-white">
                {director.name}
              </option>
            ))}
          </select>
        </div>

        {/* Actor Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-300 mb-2">
            Actor
          </label>
          <select
            value={filters.actor_id || ''}
            onChange={(e) => handleFilterChange('actor_id', e.target.value ? parseInt(e.target.value) : undefined)}
            className="w-full px-4 py-3 bg-white/5 border border-gray-600/50 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-200 appearance-none cursor-pointer"
          >
            <option value="" className="bg-gray-900 text-white">All Actors</option>
            {actors.map((actor) => (
              <option key={actor.id} value={actor.id} className="bg-gray-900 text-white">
                {actor.name}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Release Year Filter - separate row */}
      <div className="mt-4 max-w-xs">
        <label className="block text-sm font-medium text-gray-300 mb-2">
          Release Year
        </label>
        <input
          type="number"
          placeholder="e.g., 2023"
          value={filters.release_year || ''}
          onChange={(e) => handleFilterChange('release_year', e.target.value ? parseInt(e.target.value) : undefined)}
          className="w-full px-4 py-3 bg-white/5 border border-gray-600/50 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-200"
          min="1900"
          max={new Date().getFullYear()}
        />
      </div>
    </div>
  );
};
