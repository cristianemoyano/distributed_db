db1:
	docker exec -it distributed_db_shard_1_1  psql -U postgres -W postgres -d postgres

db2:
	docker exec -it distributed_db_shard_2_1  psql -U postgres -W postgres -d postgres

db3:
	docker exec -it distributed_db_shard_2_1  psql -U postgres -W postgres -d postgres

replica:
	docker exec -it distributed_db_users-replica_1 psql -U postgres -W postgres -d postgres

users:
	docker exec -it distributed_db_users_1 psql -U postgres -W postgres -d postgres

migrate:
	docker-compose run web python manage.py migrate --database=shard_1
	docker-compose run web python manage.py migrate --database=shard_2
	docker-compose run web python manage.py migrate --database=shard_3
	docker-compose run web python manage.py migrate --database=users
	docker-compose run web python manage.py migrate --database=users-replica

migrations:
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py makemigrations cars

up:
	docker-compose up --build --remove-orphans

shell:
	docker-compose run web python manage.py shell
  

resetdb:
	docker-compose run web python manage.py resetdb


superuser:
	docker-compose run web python manage.py createsuperuser


stop_replica:
	docker-compose stop users-replica

start_replica:
	docker-compose start users-replica


stop_users:
	docker-compose stop users

start_users:
	docker-compose start users