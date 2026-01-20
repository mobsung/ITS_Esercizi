package SalvataggioDatiDecorator;

public class FileDataSource implements DataSource{

    private String content;

    public FileDataSource(String content) {
        this.content = content;
    }

    @Override
    public String readData() {
        return content;
    }

    @Override
    public void writeData(String data) {
        this.content = data;
    }
}
