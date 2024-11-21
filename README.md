# grademanagementsystem

### this is student grade management system


graph TD;
    A[Main Application] --> B[Add Student];
    A --> C[Add Grade];
    A --> D[View Student Info];
    A --> E[Calculate Class Average];
    B --> F[Student Object];
    C --> F;
    D --> F;
    E --> F;
