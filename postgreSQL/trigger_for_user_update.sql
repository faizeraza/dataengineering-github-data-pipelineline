-- Create a function to handle the trigger
CREATE OR REPLACE FUNCTION update_user_dimension()
RETURNS TRIGGER AS $$
BEGIN
    -- Check if the user_name already exists in user_dimension
    IF EXISTS (SELECT 1 FROM user_dimension WHERE user_name = NEW.user_name) THEN
        -- Update the user's data
        UPDATE user_dimension
        SET
            followers = NEW.followers,
            user_location = NEW.user_location,
            total_repos = NEW.total_repos,
            total_gists = NEW.total_gists,
            email = NEW.email,
            join_date = NEW.join_date
        WHERE user_name = NEW.user_name;
        
        -- Return null to prevent the INSERT into user_dimension
        RETURN NULL;
    ELSE
        -- Insert the user's data into user_dimension
        INSERT INTO user_dimension (user_name, followers, user_location, total_repos, total_gists, email, join_date)
        VALUES (NEW.user_name, NEW.followers, NEW.user_location, NEW.total_repos, NEW.total_gists, NEW.email, NEW.join_date);
        
        -- Return the original row to proceed with the INSERT into trending_repositories_fact
        RETURN NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;
-- Create the trigger

CREATE TRIGGER insert_user_dimension_trigger
BEFORE INSERT ON user_dimension
FOR EACH ROW
EXECUTE FUNCTION update_user_dimension();