import survex3dreader

def test_reader_stations():
    data = survex3dreader.read_svx_file('./test/290.3d')
    assert abs( len(data['station_list']) - 1023 ) < 2

def test_reader_legs():
    data = survex3dreader.read_svx_file('./test/290.3d')
    assert len(data['leg_list']) > 1023

if __name__ == "__main__":
    data = survex3dreader.read_svx_file('./test/290.3d')