SELECT setval('public.rank_dimension_rank_id_seq', 1, true);
ALTER SEQUENCE public.rank_dimension_rank_id_seq CACHE 1;
SELECT setval('public.repository_dimension_repository_id_seq', 1, true);
ALTER SEQUENCE public.repository_dimension_repository_id_seq CACHE 1;
SELECT setval('public.time_dimension_time_id_seq', 1, true);
ALTER SEQUENCE public.time_dimension_time_id_seq CACHE 1;
SELECT setval('public.trending_repositories_fact_fact_id_seq', 1, true);
ALTER SEQUENCE public.trending_repositories_fact_fact_id_seq CACHE 1;
SELECT setval('public.user_dimension_user_id_seq', 1, true);
ALTER SEQUENCE public.user_dimension_user_id_seq CACHE 1;	
	