import axios from 'axios';
import { Movie, Actor, Director, Genre, MovieFilters } from '../types';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const movieApi = {
  getMovies: async (filters: MovieFilters = {}) => {
    const params = new URLSearchParams();
    
    Object.entries(filters).forEach(([key, value]: [string, any]) => {
      if (value !== undefined && value !== null && value !== '') {
        params.append(key, value.toString());
      }
    });

    const response = await api.get<Movie[]>('/movies/', { params });
    return response.data;
  },

  getMovie: async (id: number) => {
    const response = await api.get<Movie>(`/movies/${id}`);
    return response.data;
  },

  createMovie: async (movie: Partial<Movie>) => {
    const response = await api.post<Movie>('/movies/', movie);
    return response.data;
  },
};

export const actorApi = {
  getActors: async (search?: string) => {
    const params = search ? { search } : {};
    const response = await api.get<Actor[]>('/actors/', { params });
    return response.data;
  },

  getActor: async (id: number) => {
    const response = await api.get<Actor>(`/actors/${id}`);
    return response.data;
  },

  createActor: async (actor: Partial<Actor>) => {
    const response = await api.post<Actor>('/actors/', actor);
    return response.data;
  },
};

export const directorApi = {
  getDirectors: async (search?: string) => {
    const params = search ? { search } : {};
    const response = await api.get<Director[]>('/directors/', { params });
    return response.data;
  },

  getDirector: async (id: number) => {
    const response = await api.get<Director>(`/directors/${id}`);
    return response.data;
  },

  createDirector: async (director: Partial<Director>) => {
    const response = await api.post<Director>('/directors/', director);
    return response.data;
  },
};

export const genreApi = {
  getGenres: async () => {
    const response = await api.get<Genre[]>('/genres/');
    return response.data;
  },

  getGenre: async (id: number) => {
    const response = await api.get<Genre>(`/genres/${id}`);
    return response.data;
  },

  createGenre: async (genre: Partial<Genre>) => {
    const response = await api.post<Genre>('/genres/', genre);
    return response.data;
  },
};
