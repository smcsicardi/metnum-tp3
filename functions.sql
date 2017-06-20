-- SPRING, SUMMER, FALL, WINTER = 1, 2, 3, 4
CREATE OR REPLACE FUNCTION season(month integer, hemisphere integer)
    RETURNS integer AS
$$
DECLARE
    north boolean;
    result integer;
BEGIN
    north := hemisphere > 0;
    if (month in (12, 1, 2)) then
        if north then
            return 4;
        else
            return 2;
        end if;
    elsif (month in (3, 4, 5)) then
        if north then
            return 1;
        else
            return 3;
        end if;
    elsif (month in (6, 7, 8)) then
        if north then
            return 2;
        else
            return 4;
        end if;
    elsif (month in (9, 10, 11)) then
        if north then
            return 3;
        else
            return 1;
        end if;
    end if;
END;
$$
LANGUAGE 'plpgsql' IMMUTABLE;
