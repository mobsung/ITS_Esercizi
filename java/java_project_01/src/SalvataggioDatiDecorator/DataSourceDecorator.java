package SalvataggioDatiDecorator;

public abstract class DataSourceDecorator implements DataSource{

    private DataSource dataSource;

    public DataSourceDecorator(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    public DataSource getDataSource(){
        return dataSource;
    }

    @Override
    public String readData() {
        return dataSource.readData();
    }

    @Override
    public void writeData(String data) {
        dataSource.writeData(data);
    }
}
