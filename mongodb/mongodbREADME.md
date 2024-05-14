# MongoDB Studies

Commands:
- docker run --name "container_name" -d -p "port:port" "image_name"     /// example -> docker run --name mongodb_v6 -d -p 27017:27017 mongo:6.0
- docker exec -it "container_name" mongosh      /// comment: mongosh = shell terminal inside the container; example -> docker exec -it mongodb_v6 mongosh

to copy:
- docker cp "to_copy_file_name".json "container_name":/tmp/"copied_file_name".json      /// comment: copy a file from a local folder into the container; example -> docker cp example_file.json mongodb_v6:/tmp/copied_example_file.json
- docker exec "container_name" mongoimport -d "database_name" -c "collection_name" --file /tmp/"copied_file_name".json --jsonArray      /// example -> docker exec mongodb_v6 mongoimport -d my_database -c my_collection --file /tmp/copied_example_file.json --jsonArray

to use (inside the shell terminal):
- use "database_name"       /// example -> use my_database
- db."collection_name".find()       /// comment: in the database, in this specific collection, uses the "find()" method; example -> db.my_collection.find()