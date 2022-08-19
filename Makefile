db1:
	docker exec -it distributed_db_shard_1_1  psql -U postgres -W postgres -d postgres

db2:
	docker exec -it distributed_db_shard_2_1  psql -U postgres -W postgres -d postgres

db3:
	docker exec -it distributed_db_shard_2_1  psql -U postgres -W postgres -d postgres

migrate:
	docker-compose run web python manage.py migrate --database=shard_1
	docker-compose run web python manage.py migrate --database=shard_2
	docker-compose run web python manage.py migrate --database=shard_3
	docker-compose run web python manage.py migrate --database=users

migrations:
	docker-compose run web python manage.py makemigrations

up:
	docker-compose up --build --remove-orphans

shell:
	docker-compose run web python manage.py shell   

resetdb:
	docker-compose run web python manage.py resetdb


superuser:
	docker-compose run web python manage.py createsuperuser