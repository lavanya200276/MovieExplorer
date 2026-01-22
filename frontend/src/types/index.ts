export interface Genre {
  id: number;
  name: string;
  description?: string;
}

export interface Actor {
  id: number;
  name: string;
  birth_date?: string;
  bio?: string;
  photo_url?: string;
  movies?: MovieSummary[];
}

export interface Director {
  id: number;
  name: string;
  birth_date?: string;
  bio?: string;
  photo_url?: string;
  movies?: MovieSummary[];
}

export interface MovieSummary {
  id: number;
  title: string;
  release_year?: number;
  description?: string;
  poster_url?: string;
}

export interface Movie {
  id: number;
  title: string;
  release_year?: number;
  description?: string;
  poster_url?: string;
  director?: Director;
  actors: Actor[];
  genres: Genre[];
}

export interface MovieFilters {
  genre_id?: number;
  director_id?: number;
  actor_id?: number;
  release_year?: number;
  search?: string;
}
