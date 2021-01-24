import psycopg2
# from config import config

def update_visual(id, system_name, star_lum, star_metal, planet_eqtemp, star_efftemp, star_optmag, star_grav, star_mass, planet_rad, planet_eccen, planet_dens, planet_orb_per, planet_smaxis):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE main_app_visual
                SET system_name = %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (vendor_name, vendor_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    # Update vendor id 1
    update_visual(1, "test-system")
